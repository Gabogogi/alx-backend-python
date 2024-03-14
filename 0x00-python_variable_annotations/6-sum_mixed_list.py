#!/usr/bin/env python3
'''Takes a takes a list mxd_lst of integers and floats and returns their sum as a float.'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns sum of a mixed list of ints and floats'''
    return sum(mxd_lst)
