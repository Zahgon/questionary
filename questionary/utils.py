import inspect
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Set

ACTIVATED_ASYNC_MODE = False


def is_prompt_toolkit_3() -> bool:
    pass


def default_values_of(func: Callable[..., Any]) -> List[str]:
    """Return all parameter names of ``func`` with a default value."""
    pass


def arguments_of(func: Callable[..., Any]) -> List[str]:
    """Return the parameter names of the function ``func``."""
    pass


def used_kwargs(kwargs: Dict[str, Any], func: Callable[..., Any]) -> Dict[str, Any]:
    """Returns only the kwargs which can be used by a function.

    Args:
        kwargs: All available kwargs.
        func: The function which should be called.

    Returns:
        Subset of kwargs which are accepted by ``func``.
    """
    pass


def required_arguments(func: Callable[..., Any]) -> List[str]:
    """Return all arguments of a function that do not have a default value."""
    pass


def missing_arguments(func: Callable[..., Any], argdict: Dict[str, Any]) -> Set[str]:
    """Return all arguments that are missing to call func."""
    pass


async def activate_prompt_toolkit_async_mode() -> None:
    """Configure prompt toolkit to use the asyncio event loop.

    Needs to be async, so we use the right event loop in py 3.5"""
    pass
