#!/usr/bin/env python3

"""Python Annotations"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ A function that accepts a list input_list of floats
        as argument and returns their sum as a float. """
    return sum(input_list)
