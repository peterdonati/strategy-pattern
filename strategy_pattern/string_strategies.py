"""Different strategies for string manipulation"""

from abc import ABC, abstractmethod


class StringStrategy(ABC):
    """Contains instructions on how to manipulate your string"""

    @abstractmethod
    def manipulate_string(self, input_string: str):
        """Does the work of manipulating a string

        Args:
            input_string (str): the string to be manipulated
        """


class Reverse(StringStrategy):
    """Reverse the given string"""

    def manipulate_string(self, input_string: str) -> str:
        return input_string[::-1]


class EveryOther(StringStrategy):
    """Returns every other character from given string"""

    def manipulate_string(self, input_string: str) -> str:
        return input_string[::2]


class ToList(StringStrategy):
    """Puts the string in a list"""
    def manipulate_string(self, input_string: str):
        return [input_string]
