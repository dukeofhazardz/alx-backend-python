#!/usr/bin/env python3

"""Python Annotations"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ A function that accepts a list mxd_lst of integers
        and floats and returns their sum as a float. """
    return float(sum(mxd_lst))
