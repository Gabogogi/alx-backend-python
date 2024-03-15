#!/usr/bin/env python3
'''Type annotation for a list of floats'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns sum of list as a float'''
    return sum(input_list)
