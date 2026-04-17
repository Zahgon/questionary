from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from prompt_toolkit.completion import CompleteEvent
from prompt_toolkit.completion import Completer
from prompt_toolkit.completion import Completion
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.lexers import SimpleLexer
from prompt_toolkit.shortcuts.prompt import CompleteStyle
from prompt_toolkit.shortcuts.prompt import PromptSession
from prompt_toolkit.styles import Style

from questionary.constants import DEFAULT_QUESTION_PREFIX
from questionary.prompts.common import build_validator
from questionary.question import Question
from questionary.styles import merge_styles_default


class WordCompleter(Completer):
    choices_source: Union[List[str], Callable[[], List[str]]]
    ignore_case: bool
    meta_information: Dict[str, Any]
    match_middle: bool

    def __init__(
        self,
        choices: Union[List[str], Callable[[], List[str]]],
        ignore_case: bool = True,
        meta_information: Optional[Dict[str, Any]] = None,
        match_middle: bool = True,
    ) -> None:
        self.choices_source = choices
        self.ignore_case = ignore_case
        self.meta_information = meta_information or {}
        self.match_middle = match_middle

    def _choices(self) -> Iterable[str]:
        pass

    def _choice_matches(self, word_before_cursor: str, choice: str) -> int:
        """Match index if found, -1 if not."""
        pass

    @staticmethod
    def _display_for_choice(choice: str, index: int, word_before_cursor: str) -> HTML:
        pass

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        pass


def autocomplete(
    message: str,
    choices: List[str],
    default: str = "",
    qmark: str = DEFAULT_QUESTION_PREFIX,
    completer: Optional[Completer] = None,
    meta_information: Optional[Dict[str, Any]] = None,
    ignore_case: bool = True,
    match_middle: bool = True,
    complete_style: CompleteStyle = CompleteStyle.COLUMN,
    validate: Any = None,
    style: Optional[Style] = None,
    **kwargs: Any,
) -> Question:
    """Prompt the user to enter a message with autocomplete help.

    Example:
        >>> import questionary
        >>> questionary.autocomplete(
        ...    'Choose ant species',
        ...    choices=[
        ...         'Camponotus pennsylvanicus',
        ...         'Linepithema humile',
        ...         'Eciton burchellii',
        ...         "Atta colombica",
        ...         'Polyergus lucidus',
        ...         'Polyergus rufescens',
        ...    ]).ask()
        ? Choose ant species Atta colombica
        'Atta colombica'

    .. image:: ../images/autocomplete.gif

    This is just a really basic example, the prompt can be customised using the
    parameters.


    Args:
        message: Question text

        choices: Items shown in the selection, this contains items as strings

        default: Default return value (single value).

        qmark: Question prefix displayed in front of the question.
               By default this is a ``?``

        completer: A prompt_toolkit :class:`prompt_toolkit.completion.Completion`
                   implementation. If not set, a questionary completer implementation
                   will be used.

        meta_information: A dictionary with information/anything about choices.

        ignore_case: If true autocomplete would ignore case.

        match_middle: If true autocomplete would search in every string position
                      not only in string begin.

        complete_style: How autocomplete menu would be shown, it could be ``COLUMN``
                        ``MULTI_COLUMN`` or ``READLINE_LIKE`` from
                        :class:`prompt_toolkit.shortcuts.CompleteStyle`.

        validate: Require the entered value to pass a validation. The
                  value can not be submitted until the validator accepts
                  it (e.g. to check minimum password length).

                  This can either be a function accepting the input and
                  returning a boolean, or an class reference to a
                  subclass of the prompt toolkit Validator class.

        style: A custom color and style for the question parts. You can
               configure colors as well as font types for different elements.

    Returns:
        :class:`Question`: Question instance, ready to be prompted (using ``.ask()``).
    """
    pass
