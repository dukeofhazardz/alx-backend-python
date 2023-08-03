#!/usr/bin/env python3

"""Python Annotations"""

from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
      -> Union[Any, T]:
    """Annotating all variables"""
    if key in dct:
        return dct[key]
    else:
        return default
