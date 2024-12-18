from collections import namedtuple
from queue import Queue
from typing import Callable

# Custom Types
FunctionTrace = namedtuple("FunctionTrace", ["name", "args", "kwargs", "retval"])

# Save overriden functions for passthrough purposes.
_print = print

# Storage mechanism for all function calls.
func_calls = Queue()

##
# Utils
##
class _Colors:
    CYAN    = "\033[36m"
    GREEN   = "\033[32m"
    RED     = "\033[31m"
    YELLOW  = "\033[33m"
    RESET   = "\033[0m"

def print_fail(msg: str):
    _print(f"❌ {_Colors.RED}Oh no! {msg}{_Colors.RESET}")

def print_ok(msg: str):
    _print(f"✅ {_Colors.GREEN}Great! {msg}{_Colors.RESET}")

def _store_call(wrapped:Callable):
    """Records function call for later examination.

    Args:
        wrapped : the function to track. 

    Note:
        Implemented to be used as a decorator.
    """

    
    def wrapper(*args, **kwargs):
        """Forward all function parameters to wrapped function.
        """
        retval = wrapped(*args, **kwargs)
        func_calls.put(FunctionTrace(name=wrapped.__name__, args=args, kwargs=kwargs, retval=retval))
        return retval

    return wrapper


@_store_call
def print(*args, **kwargs):
    _print(*args, **kwargs)

@_store_call
def add(one, two):
    return one+two

