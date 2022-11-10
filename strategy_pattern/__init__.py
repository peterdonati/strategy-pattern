"""A package for manipulating strings different ways."""

from strategy_pattern.string_manipulator import StringManipulator
from strategy_pattern.string_strategies import (
    StringStrategy,
    Reverse,
    EveryOther,
    ToList
)


__all__ = [
    'StringManipulator',
    'StringStrategy',
    'Reverse',
    'EveryOther',
    'ToList'
]
