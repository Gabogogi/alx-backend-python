#!/usr/bin/env python3
'''Annotates a given function'''
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Type annotation for an iterable'''
    return [(i, len(i)) for i in lst]
