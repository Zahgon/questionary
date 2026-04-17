from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Mapping
from typing import Optional
from typing import Union

from prompt_toolkit.output import ColorDepth

from questionary import utils
from questionary.constants import DEFAULT_KBI_MESSAGE
from questionary.prompts import AVAILABLE_PROMPTS
from questionary.prompts import prompt_by_name
from questionary.prompts.common import print_formatted_text
from questionary.question import Question


class PromptParameterException(ValueError):
    """Received a prompt with a missing parameter."""

    def __init__(self, message: str, errors: Optional[BaseException] = None) -> None:
        # Call the base class constructor with the parameters it needs
        super().__init__(f"You must provide a `{message}` value", errors)


def parse_question_config(
    question_config, answers, patch_stdout, true_color, **kwargs: Any
) -> Optional[tuple[Question, Callable[[Any], None]]]:
    """Create a question based on the configuration for a prompt

    Args:
        question_config: A configuration dictionary for a single question
        answers: Default answers.

        patch_stdout: Ensure that the prompt renders correctly if other threads
                      are printing to stdout.

        true_color: Use true color output.

    Returns:
        A question to be asked and a callable to handle the answer
    """
    pass


async def prompt_async(
    questions: Union[Dict[str, Any], Iterable[Mapping[str, Any]]],
    answers: Optional[Mapping[str, Any]] = None,
    patch_stdout: bool = False,
    true_color: bool = False,
    kbi_msg: str = DEFAULT_KBI_MESSAGE,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Prompt the user for input on all the questions using asyncio.

    Catches keyboard interrupts and prints a message.

    See :func:`unsafe_prompt_async` for possible question configurations.

    Args:
        questions: A list of question configs representing questions to
                   ask. A question config may have the following options:

                   * type - The type of question.
                   * name - An ID for the question (to identify it in the answers :obj:`dict`).

                   * when - Callable to conditionally show the question. This function
                     takes a :obj:`dict` representing the current answers.

                   * filter - Function that the answer is passed to. The return value of this
                     function is saved as the answer.

                   Additional options correspond to the parameter names for
                   particular question types.

        answers: Default answers.

        patch_stdout: Ensure that the prompt renders correctly if other threads
                      are printing to stdout.

        kbi_msg: The message to be printed on a keyboard interrupt.
        true_color: Use true color output.

        color_depth: Color depth to use. If ``true_color`` is set to true then this
                     value is ignored.

        type: Default ``type`` value to use in question config.
        filter: Default ``filter`` value to use in question config.
        name: Default ``name`` value to use in question config.
        when: Default ``when`` value to use in question config.
        default: Default ``default`` value to use in question config.
        kwargs: Additional options passed to every question.

    Returns:
        Dictionary of question answers.
    """
    pass


def prompt(
    questions: Union[Dict[str, Any], Iterable[Mapping[str, Any]]],
    answers: Optional[Mapping[str, Any]] = None,
    patch_stdout: bool = False,
    true_color: bool = False,
    kbi_msg: str = DEFAULT_KBI_MESSAGE,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Prompt the user for input on all the questions.

    Catches keyboard interrupts and prints a message.

    See :func:`unsafe_prompt` for possible question configurations.

    Args:
        questions: A list of question configs representing questions to
                   ask. A question config may have the following options:

                   * type - The type of question.
                   * name - An ID for the question (to identify it in the answers :obj:`dict`).

                   * when - Callable to conditionally show the question. This function
                     takes a :obj:`dict` representing the current answers.

                   * filter - Function that the answer is passed to. The return value of this
                     function is saved as the answer.

                   Additional options correspond to the parameter names for
                   particular question types.

        answers: Default answers.

        patch_stdout: Ensure that the prompt renders correctly if other threads
                      are printing to stdout.

        kbi_msg: The message to be printed on a keyboard interrupt.
        true_color: Use true color output.

        color_depth: Color depth to use. If ``true_color`` is set to true then this
                     value is ignored.

        type: Default ``type`` value to use in question config.
        filter: Default ``filter`` value to use in question config.
        name: Default ``name`` value to use in question config.
        when: Default ``when`` value to use in question config.
        default: Default ``default`` value to use in question config.
        kwargs: Additional options passed to every question.

    Returns:
        Dictionary of question answers.
    """
    pass


async def unsafe_prompt_async(
    questions: Union[Dict[str, Any], Iterable[Mapping[str, Any]]],
    answers: Optional[Mapping[str, Any]] = None,
    patch_stdout: bool = False,
    true_color: bool = False,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Prompt the user for input on all the questions using asyncio.

    Won't catch keyboard interrupts.

    Args:
        questions: A list of question configs representing questions to
                   ask. A question config may have the following options:

                   * type - The type of question.
                   * name - An ID for the question (to identify it in the answers :obj:`dict`).

                   * when - Callable to conditionally show the question. This function
                     takes a :obj:`dict` representing the current answers.

                   * filter - Function that the answer is passed to. The return value of this
                     function is saved as the answer.

                   Additional options correspond to the parameter names for
                   particular question types.

        answers: Default answers.

        patch_stdout: Ensure that the prompt renders correctly if other threads
                      are printing to stdout.

        true_color: Use true color output.

        color_depth: Color depth to use. If ``true_color`` is set to true then this
                     value is ignored.

        type: Default ``type`` value to use in question config.
        filter: Default ``filter`` value to use in question config.
        name: Default ``name`` value to use in question config.
        when: Default ``when`` value to use in question config.
        default: Default ``default`` value to use in question config.
        kwargs: Additional options passed to every question.

    Returns:
        Dictionary of question answers.

    Raises:
        KeyboardInterrupt: raised on keyboard interrupt
    """
    pass


def unsafe_prompt(
    questions: Union[Dict[str, Any], Iterable[Mapping[str, Any]]],
    answers: Optional[Mapping[str, Any]] = None,
    patch_stdout: bool = False,
    true_color: bool = False,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Prompt the user for input on all the questions.

    Won't catch keyboard interrupts.

    Args:
        questions: A list of question configs representing questions to
                   ask. A question config may have the following options:

                   * type - The type of question.
                   * name - An ID for the question (to identify it in the answers :obj:`dict`).

                   * when - Callable to conditionally show the question. This function
                     takes a :obj:`dict` representing the current answers.

                   * filter - Function that the answer is passed to. The return value of this
                     function is saved as the answer.

                   Additional options correspond to the parameter names for
                   particular question types.

        answers: Default answers.

        patch_stdout: Ensure that the prompt renders correctly if other threads
                      are printing to stdout.

        true_color: Use true color output.

        color_depth: Color depth to use. If ``true_color`` is set to true then this
                     value is ignored.

        type: Default ``type`` value to use in question config.
        filter: Default ``filter`` value to use in question config.
        name: Default ``name`` value to use in question config.
        when: Default ``when`` value to use in question config.
        default: Default ``default`` value to use in question config.
        kwargs: Additional options passed to every question.

    Returns:
        Dictionary of question answers.

    Raises:
        KeyboardInterrupt: raised on keyboard interrupt
    """
    pass
