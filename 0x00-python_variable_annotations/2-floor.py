#!/usr/bin/env python3

"""Write a type-annotated function floor which takes a float "n"
    as argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """Basic annotations - floor
        Arg:
          n: float
          str2: str
        Return: the float value of n: int
    """
    return math.floor(n)
