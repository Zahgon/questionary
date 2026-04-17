import inspect
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

from prompt_toolkit import PromptSession
from prompt_toolkit.filters import Always
from prompt_toolkit.filters import Condition
from prompt_toolkit.filters import IsDone
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout import ConditionalContainer
from prompt_toolkit.layout import FormattedTextControl
from prompt_toolkit.layout import HSplit
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout import Window
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.layout.dimension import LayoutDimension
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import ValidationError
from prompt_toolkit.validation import Validator

from questionary.constants import DEFAULT_SELECTED_POINTER
from questionary.constants import DEFAULT_STYLE
from questionary.constants import INDICATOR_SELECTED
from questionary.constants import INDICATOR_UNSELECTED
from questionary.constants import INVALID_INPUT

# This is a cut-down version of `prompt_toolkit.formatted_text.AnyFormattedText`
# which does not exist in v2 of prompt_toolkit
FormattedText = Union[
    str,
    List[Tuple[str, str]],
    List[Tuple[str, str, Callable[[Any], None]]],
    None,
]


class Choice:
    """One choice in a :meth:`select`, :meth:`rawselect` or :meth:`checkbox`.

    Args:
        title: Text shown in the selection list.

        value: Value returned, when the choice is selected. If this argument
               is `None` or unset, then the value of `title` is used.

        disabled: If set, the choice can not be selected by the user. The
                  provided text is used to explain why the selection is
                  disabled or, if a boolean, no explanation is provided.

        checked: Preselect this choice when displaying the options.

        shortcut_key: Key shortcut used to select this item.

        description: Optional description of the item that can be displayed.
    """

    title: FormattedText
    """Display string for the choice"""

    value: Optional[Any]
    """Value of the choice"""

    disabled: Optional[Union[str, bool]]
    """Whether the choice can be selected"""

    checked: Optional[bool]
    """Whether the choice is initially selected"""

    __shortcut_key: Optional[Union[str, bool]]

    description: Optional[str]
    """Choice description"""

    def __init__(
        self,
        title: FormattedText,
        value: Optional[Any] = None,
        disabled: Optional[Union[str, bool]] = None,
        checked: Optional[bool] = False,
        shortcut_key: Optional[Union[str, bool]] = True,
        description: Optional[str] = None,
    ) -> None:
        self.disabled = disabled
        self.title = title
        self.shortcut_key = shortcut_key
        # self.auto_shortcut is set by the self.shortcut_key setter
        self.checked = checked if checked is not None else False
        self.description = description

        if value is not None:
            self.value = value
        elif isinstance(title, list):
            self.value = "".join([token[1] for token in title])
        else:
            self.value = title

    @staticmethod
    def build(c: Union[str, "Choice", Dict[str, Any]]) -> "Choice":
        """Create a choice object from different representations.

        Args:
            c: Either a :obj:`str`, :class:`Choice` or :obj:`dict` with
               ``name``, ``value``, ``disabled``, ``checked`` and
               ``key`` properties.

        Returns:
            An instance of the :class:`Choice` object.
        """
        pass

    @property
    def shortcut_key(self) -> Optional[Union[str, bool]]:
        """A shortcut key for the choice"""
        pass

    @shortcut_key.setter
    def shortcut_key(self, key: Optional[Union[str, bool]]):
        pass

    @shortcut_key.deleter
    def shortcut_key(self):
        pass

    def get_shortcut_title(self):
        pass

    @property
    def auto_shortcut(self) -> bool:
        """Whether to assign a shortcut key to the choice

        Keys are assigned starting with numbers and proceeding
        through the ASCII alphabet.
        """
        pass

    @auto_shortcut.setter
    def auto_shortcut(self, should_assign: bool):
        pass

    @auto_shortcut.deleter
    def auto_shortcut(self):
        pass


class Separator(Choice):
    """Used to space/separate choices group."""

    default_separator: str = "-" * 15
    """The default separator used if none is specified"""

    line: str
    """The string being used as a separator"""

    def __init__(self, line: Optional[str] = None) -> None:
        """Create a separator in a list.

        Args:
            line: Text to be displayed in the list, by default uses ``---``.
        """

        self.line = line or self.default_separator
        super().__init__(self.line, None, "-")


class InquirerControl(FormattedTextControl):
    SHORTCUT_KEYS = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    choices: List[Choice]
    default: Optional[Union[str, Choice, Dict[str, Any]]]
    selected_options: List[Any]
    search_filter: Union[str, None] = None
    use_indicator: bool
    use_shortcuts: bool
    use_arrow_keys: bool
    pointer: Optional[str]
    pointed_at: int
    is_answered: bool
    show_description: bool

    def __init__(
        self,
        choices: Sequence[Union[str, Choice, Dict[str, Any]]],
        default: Optional[Union[str, Choice, Dict[str, Any]]] = None,
        pointer: Optional[str] = DEFAULT_SELECTED_POINTER,
        use_indicator: bool = True,
        use_shortcuts: bool = False,
        show_selected: bool = False,
        show_description: bool = True,
        use_arrow_keys: bool = True,
        initial_choice: Optional[Union[str, Choice, Dict[str, Any]]] = None,
        **kwargs: Any,
    ):
        self.use_indicator = use_indicator
        self.use_shortcuts = use_shortcuts
        self.show_selected = show_selected
        self.show_description = show_description
        self.use_arrow_keys = use_arrow_keys
        self.default = default
        self.pointer = pointer

        if isinstance(default, Choice):
            default = default.value

        choices_values = [
            choice.value for choice in choices if isinstance(choice, Choice)
        ]

        if (
            default is not None
            and default not in choices
            and default not in choices_values
        ):
            raise ValueError(
                f"Invalid `default` value passed. The value (`{default}`) "
                f"does not exist in the set of choices. Please make sure the "
                f"default value is one of the available choices."
            )

        if initial_choice is None:
            pointed_at = None
        elif initial_choice in choices:
            pointed_at = choices.index(initial_choice)
        elif initial_choice in choices_values:
            for k, choice in enumerate(choices):
                if isinstance(choice, Choice):
                    if choice.value == initial_choice:
                        pointed_at = k
                        break

        else:
            raise ValueError(
                f"Invalid `initial_choice` value passed. The value "
                f"(`{initial_choice}`) does not exist in "
                f"the set of choices. Please make sure the initial value is "
                f"one of the available choices."
            )

        self.is_answered = False
        self.choices = []
        self.submission_attempted = False
        self.error_message = None
        self.selected_options = []
        self.found_in_search = False

        self._init_choices(choices, pointed_at)
        self._assign_shortcut_keys()

        super().__init__(self._get_choice_tokens, **kwargs)

        if not self.is_selection_valid():
            raise ValueError(
                f"Invalid 'initial_choice' value ('{initial_choice}'). "
                f"It must be a selectable value."
            )

    def _is_selected(self, choice: Choice):
        pass

    def _assign_shortcut_keys(self):
        pass

    def _init_choices(
        self,
        choices: Sequence[Union[str, Choice, Dict[str, Any]]],
        pointed_at: Optional[int],
    ):
        # helper to convert from question format to internal format
        pass

    @property
    def filtered_choices(self):
        pass

    @property
    def choice_count(self) -> int:
        pass

    def _get_choice_tokens(self):
        pass

    def is_selection_a_separator(self) -> bool:
        pass

    def is_selection_disabled(self) -> Optional[Union[str, bool]]:
        pass

    def is_selection_valid(self) -> bool:
        pass

    def select_previous(self) -> None:
        pass

    def select_next(self) -> None:
        pass

    def get_pointed_at(self) -> Choice:
        pass

    def get_selected_values(self) -> List[Choice]:
        # get values not labels
        pass

    def add_search_character(self, char: Keys) -> None:
        """Adds a character to the search filter"""
        pass

    def remove_search_character(self) -> None:
        pass

    def get_search_string_tokens(self):
        pass


def build_validator(validate: Any) -> Optional[Validator]:
    pass


def _fix_unecessary_blank_lines(ps: PromptSession) -> None:
    """This is a fix for additional empty lines added by prompt toolkit.

    This assumes the layout of the default session doesn't change, if it
    does, this needs an update."""
    pass


def create_inquirer_layout(
    ic: InquirerControl,
    get_prompt_tokens: Callable[[], List[Tuple[str, str]]],
    **kwargs: Any,
) -> Layout:
    """Create a layout combining question and inquirer selection."""
    pass


def print_formatted_text(text: str, style: Optional[str] = None, **kwargs: Any) -> None:
    """Print formatted text.

    Sometimes you want to spice up your printed messages a bit,
    :meth:`questionary.print` is a helper to do just that.

    Example:

        >>> import questionary
        >>> questionary.print("Hello World 🦄", style="bold italic fg:darkred")
        Hello World 🦄

    .. image:: ../images/print.gif

    Args:
        text: Text to be printed.
        style: Style used for printing. The style argument uses the
            prompt :ref:`toolkit style strings <prompt_toolkit:styling>`.
    """
    pass
