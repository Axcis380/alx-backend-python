#!/usr/bin/env python3
'''task 10 mod.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''retrieve the first elem of seq if it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
