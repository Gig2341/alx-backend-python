#!/usr/bin/env python3


"""
this module function sum_mixed_list which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' this function returns a sum of a  list integers and floats'''
    return sum(mxd_lst)
