from typing import Callable
from oj import ns_timestamp

def timed(func: Callable[[], None]) -> Callable[[], int]:
    def inner_function():
        a = ns_timestamp()
        func()
        return ns_timestamp() - a

    return inner_function
