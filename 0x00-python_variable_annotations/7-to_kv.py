#!/usr/bin/env python3
'''task 7 module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''converts a key nd it value to tuple of key and
    the square of it val.
    '''
    return (k, float(v**2))
