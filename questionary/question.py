import sys
from typing import Any

import prompt_toolkit.patch_stdout
from prompt_toolkit import Application

from questionary import utils
from questionary.constants import DEFAULT_KBI_MESSAGE


class Question:
    """A question to be prompted.

    This is an internal class. Questions should be created using the
    predefined questions (e.g. text or password)."""

    application: "Application[Any]"
    should_skip_question: bool
    default: Any

    def __init__(self, application: "Application[Any]") -> None:
        self.application = application
        self.should_skip_question = False
        self.default = None

    async def ask_async(
        self, patch_stdout: bool = False, kbi_msg: str = DEFAULT_KBI_MESSAGE
    ) -> Any:
        """Ask the question using asyncio and return user response.

        Args:
            patch_stdout: Ensure that the prompt renders correctly if other threads
                          are printing to stdout.

            kbi_msg: The message to be printed on a keyboard interrupt.

        Returns:
            `Any`: The answer from the question.
        """
        pass

    def ask(
        self, patch_stdout: bool = False, kbi_msg: str = DEFAULT_KBI_MESSAGE
    ) -> Any:
        """Ask the question synchronously and return user response.

        Args:
            patch_stdout: Ensure that the prompt renders correctly if other threads
                          are printing to stdout.

            kbi_msg: The message to be printed on a keyboard interrupt.

        Returns:
            `Any`: The answer from the question.
        """
        pass

    def unsafe_ask(self, patch_stdout: bool = False) -> Any:
        """Ask the question synchronously and return user response.

        Does not catch keyboard interrupts.

        Args:
            patch_stdout: Ensure that the prompt renders correctly if other threads
                          are printing to stdout.

        Returns:
            `Any`: The answer from the question.
        """
        pass

    def skip_if(self, condition: bool, default: Any = None) -> "Question":
        """Skip the question if flag is set and return the default instead.

        Args:
            condition: A conditional boolean value.
            default: The default value to return.

        Returns:
            :class:`Question`: `self`.
        """
        pass

    async def unsafe_ask_async(self, patch_stdout: bool = False) -> Any:
        """Ask the question using asyncio and return user response.

        Does not catch keyboard interrupts.

        Args:
            patch_stdout: Ensure that the prompt renders correctly if other threads
                          are printing to stdout.

        Returns:
            `Any`: The answer from the question.
        """
        pass
