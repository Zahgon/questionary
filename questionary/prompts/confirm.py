from typing import Any
from typing import Optional

from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import to_formatted_text
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import Style

from questionary.constants import DEFAULT_QUESTION_PREFIX
from questionary.constants import NO
from questionary.constants import NO_OR_YES
from questionary.constants import YES
from questionary.constants import YES_OR_NO
from questionary.question import Question
from questionary.styles import merge_styles_default


def confirm(
    message: str,
    default: bool = True,
    qmark: str = DEFAULT_QUESTION_PREFIX,
    style: Optional[Style] = None,
    auto_enter: bool = True,
    instruction: Optional[str] = None,
    **kwargs: Any,
) -> Question:
    """A yes or no question. The user can either confirm or deny.

    This question type can be used to prompt the user for a confirmation
    of a yes-or-no question. If the user just hits enter, the default
    value will be returned.

    Example:
        >>> import questionary
        >>> questionary.confirm("Are you amazed?").ask()
        ? Are you amazed? Yes
        True

    .. image:: ../images/confirm.gif

    This is just a really basic example, the prompt can be customised using the
    parameters.


    Args:
        message: Question text.

        default: Default value will be returned if the user just hits
                 enter.

        qmark: Question prefix displayed in front of the question.
               By default this is a ``?``.

        style: A custom color and style for the question parts. You can
               configure colors as well as font types for different elements.

        auto_enter: If set to `False`, the user needs to press the 'enter' key to
            accept their answer. If set to `True`, a valid input will be
            accepted without the need to press 'Enter'.

        instruction: A message describing how to proceed through the
                     confirmation prompt.
    Returns:
        :class:`Question`: Question instance, ready to be prompted (using `.ask()`).
    """
    pass
