#!/usr/bin/env python3
'''task 9 mod.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''compute the length of list of seq.
    '''
    return [(i, len(i)) for i in lst]
