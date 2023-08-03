#!/usr/bin/env python3

"""Python Annotations"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating all variables"""
    return [(i, len(i)) for i in lst]
