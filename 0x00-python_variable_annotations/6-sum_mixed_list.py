#!/usr/bin/env python3

"""Write a type-annotated function sum_mixed_list which takes a list "mxd_lst"
    of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Complex types - list of floats
        Arg:
          input_list: floats
        Return: the sum of items in the list: float
    """
    return sum(mxd_list)
