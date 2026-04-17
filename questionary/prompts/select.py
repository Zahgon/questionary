# -*- coding: utf-8 -*-

import string
from typing import Any
from typing import Dict
from typing import Optional
from typing import Sequence
from typing import Union

from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import Style

from questionary import utils
from questionary.constants import DEFAULT_QUESTION_PREFIX
from questionary.constants import DEFAULT_SELECTED_POINTER
from questionary.prompts import common
from questionary.prompts.common import Choice
from questionary.prompts.common import InquirerControl
from questionary.prompts.common import Separator
from questionary.question import Question
from questionary.styles import merge_styles_default


def select(
    message: str,
    choices: Sequence[Union[str, Choice, Dict[str, Any]]],
    default: Optional[Union[str, Choice, Dict[str, Any]]] = None,
    qmark: str = DEFAULT_QUESTION_PREFIX,
    pointer: Optional[str] = DEFAULT_SELECTED_POINTER,
    style: Optional[Style] = None,
    use_shortcuts: bool = False,
    use_arrow_keys: bool = True,
    use_indicator: bool = False,
    use_jk_keys: bool = True,
    use_emacs_keys: bool = True,
    use_search_filter: bool = False,
    show_selected: bool = False,
    show_description: bool = True,
    instruction: Optional[str] = None,
    **kwargs: Any,
) -> Question:
    """A list of items to select **one** option from.

    The user can pick one option and confirm it (if you want to allow
    the user to select multiple options, use :meth:`questionary.checkbox` instead).

    Example:
        >>> import questionary
        >>> questionary.select(
        ...     "What do you want to do?",
        ...     choices=[
        ...         "Order a pizza",
        ...         "Make a reservation",
        ...         "Ask for opening hours"
        ...     ]).ask()
        ? What do you want to do? Order a pizza
        'Order a pizza'

    .. image:: ../images/select.gif

    This is just a really basic example, the prompt can be customised using the
    parameters.


    Args:
        message: Question text

        choices: Items shown in the selection, this can contain :class:`Choice` or
                 or :class:`Separator` objects or simple items as strings. Passing
                 :class:`Choice` objects, allows you to configure the item more
                 (e.g. preselecting it or disabling it).

        default: A value corresponding to a selectable item in the choices,
                 to initially set the pointer position to.

        qmark: Question prefix displayed in front of the question.
               By default this is a ``?``.

        pointer: Pointer symbol in front of the currently highlighted element.
                 By default this is a ``»``.
                 Use ``None`` to disable it.

        instruction: A hint on how to navigate the menu.
                     It's ``(Use shortcuts)`` if only ``use_shortcuts`` is set
                     to True, ``(Use arrow keys or shortcuts)`` if ``use_arrow_keys``
                     & ``use_shortcuts`` are set and ``(Use arrow keys)`` by default.

        style: A custom color and style for the question parts. You can
               configure colors as well as font types for different elements.

        use_indicator: Flag to enable the small indicator in front of the
                       list highlighting the current location of the selection
                       cursor.

        use_shortcuts: Allow the user to select items from the list using
                       shortcuts. The shortcuts will be displayed in front of
                       the list items. Arrow keys, j/k keys and shortcuts are
                       not mutually exclusive.

        use_arrow_keys: Allow the user to select items from the list using
                        arrow keys. Arrow keys, j/k keys and shortcuts are not
                        mutually exclusive.

        use_jk_keys: Allow the user to select items from the list using
                     `j` (down) and `k` (up) keys. Arrow keys, j/k keys and
                     shortcuts are not mutually exclusive.

        use_emacs_keys: Allow the user to select items from the list using
                        `Ctrl+N` (down) and `Ctrl+P` (up) keys. Arrow keys, j/k keys,
                        emacs keys and shortcuts are not mutually exclusive.

        use_search_filter: Flag to enable search filtering. Typing some string will
                           filter the choices to keep only the ones that contain the
                           search string.
                           Note that activating this option disables "vi-like"
                           navigation as "j" and "k" can be part of a prefix and
                           therefore cannot be used for navigation

        show_selected: Display current selection choice at the bottom of list.

        show_description: Display description of current selection if available.

    Returns:
        :class:`Question`: Question instance, ready to be prompted (using ``.ask()``).
    """
    pass
