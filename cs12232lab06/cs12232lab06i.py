from typing import Callable
from oj import ns_timestamp

worst = -1

def worst_case_timed(func: Callable[[], None]) -> Callable[[], int]:
    def inner_function():
        global worst

        first_call = ns_timestamp()
        func()
        last_call = ns_timestamp()

        call_time = last_call-first_call

        worst = max(worst, call_time)

        return worst

    return inner_function