import string
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

from prompt_toolkit.application import Application
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import Style

from questionary import utils
from questionary.constants import DEFAULT_QUESTION_PREFIX
from questionary.constants import DEFAULT_SELECTED_POINTER
from questionary.constants import INVALID_INPUT
from questionary.prompts import common
from questionary.prompts.common import Choice
from questionary.prompts.common import InquirerControl
from questionary.prompts.common import Separator
from questionary.question import Question
from questionary.styles import merge_styles_default


def checkbox(
    message: str,
    choices: Sequence[Union[str, Choice, Dict[str, Any]]],
    default: Optional[str] = None,
    validate: Callable[[List[str]], Union[bool, str]] = lambda a: True,
    qmark: str = DEFAULT_QUESTION_PREFIX,
    pointer: Optional[str] = DEFAULT_SELECTED_POINTER,
    style: Optional[Style] = None,
    initial_choice: Optional[Union[str, Choice, Dict[str, Any]]] = None,
    use_arrow_keys: bool = True,
    use_jk_keys: bool = True,
    use_emacs_keys: bool = True,
    use_search_filter: bool = False,
    instruction: Optional[str] = None,
    show_description: bool = True,
    cycle_list: bool = True,
    **kwargs: Any,
) -> Question:
    """Ask the user to select from a list of items.

    This is a multiselect, the user can choose one, none or many of the
    items.

    Example:
        >>> import questionary
        >>> questionary.checkbox(
        ...    'Select toppings',
        ...    choices=[
        ...        "Cheese",
        ...        "Tomato",
        ...        "Pineapple",
        ...    ]).ask()
        ? Select toppings done (2 selections)
        ['Cheese', 'Pineapple']

    .. image:: ../images/checkbox.gif

    This is just a really basic example, the prompt can be customised using the
    parameters.


    Args:
        message: Question text

        choices: Items shown in the selection, this can contain :class:`Choice` or
                 or :class:`Separator` objects or simple items as strings. Passing
                 :class:`Choice` objects, allows you to configure the item more
                 (e.g. preselecting it or disabling it).

        default: Default return value (single value). If you want to preselect
                 multiple items, use ``Choice("foo", checked=True)`` instead.

        validate: Require the entered value to pass a validation. The
                  value can not be submitted until the validator accepts
                  it (e.g. to check minimum password length).

                  This should be a function accepting the input and
                  returning a boolean. Alternatively, the return value
                  may be a string (indicating failure), which contains
                  the error message to be displayed.

        qmark: Question prefix displayed in front of the question.
               By default this is a ``?``.

        pointer: Pointer symbol in front of the currently highlighted element.
                 By default this is a ``»``.
                 Use ``None`` to disable it.

        style: A custom color and style for the question parts. You can
               configure colors as well as font types for different elements.

        initial_choice: A value corresponding to a selectable item in the choices,
                        to initially set the pointer position to.

        use_arrow_keys: Allow the user to select items from the list using
                        arrow keys.

        use_jk_keys: Allow the user to select items from the list using
                     `j` (down) and `k` (up) keys.

        use_emacs_keys: Allow the user to select items from the list using
                        `Ctrl+N` (down) and `Ctrl+P` (up) keys.

        use_search_filter: Flag to enable search filtering. Typing some string will
                           filter the choices to keep only the ones that contain the
                           search string.
                           Note that activating this option disables "vi-like"
                           navigation as "j" and "k" can be part of a prefix and
                           therefore cannot be used for navigation

        instruction: A message describing how to navigate the menu.

        show_description: Display description of current selection if available.

        cycle_list: When True, allows cursor to wrap from last item to first (and vice versa).
                    When False, cursor stops at the ends and does not wrap around.
                    Default is True.

    Returns:
        :class:`Question`: Question instance, ready to be prompted (using ``.ask()``).
    """
    pass
