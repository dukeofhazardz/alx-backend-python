#!/usr/bin/env python3

"""Python Annotations"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ A function that accepts a  takes a float multiplier as argument and
        returns a function that multiplies a float by multiplier. """

    def multiply(x: float) -> float:
        """A function that multiplies a float with a multiplier"""
        return multiplier * x

    return multiply
