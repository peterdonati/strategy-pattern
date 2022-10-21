"""stuff happens here"""

from strategy_pattern.string_strategies import StringStrategy


class StringManipulator():
    """Create a string manipulator class with the desired strategy.

    Args:
        input_string (str): string to be manipulated
        strategy (StringStrategy): strategy to use to maniuplate string
    """

    def __init__(self, input_string:str, strategy:StringStrategy) -> None:
        self.input_string = input_string
        self._strategy = strategy

    @property
    def strategy(self) -> StringStrategy:
        """Create a strategy property so that the desired strategy can be
        changed after class is created
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StringStrategy) -> None:
        self._strategy = strategy

    def process_string(self) -> str:
        """Process your input string

        Returns:
            str: your processed input string
        """
        return self._strategy.manipulate_string(self.input_string)
