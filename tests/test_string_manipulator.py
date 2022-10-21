"""Unit tests for string_manipulator and its dependencies"""
import unittest
from strategy_pattern import (
    StringManipulator,
    StringStrategy,
    Reverse,
    EveryOther,
    ToList
)


class TestStringManipulator(unittest.TestCase):
    """Unit testing for StringManipulator class"""
    def setUp(self) -> None:
        self.manipulator = StringManipulator('goodbye', Reverse())

    def test_string_manipulator_creation(self):
        self.assertIsInstance(self.manipulator, StringManipulator)

    def test_process_string(self):
        self.assertEqual('eybdoog', self.manipulator.process_string())

    def test_manipulator_change_strategy(self):
        self.assertEqual(self.manipulator.strategy.__class__, Reverse().__class__)
        self.manipulator.strategy = ToList()
        self.assertEqual(self.manipulator.strategy.__class__, ToList().__class__)


class TestStrategies(unittest.TestCase):
    """Tests for strategies funcioning correctly"""
    def test_cant_instantiate(self):
        with self.assertRaises(TypeError):
            StringStrategy()

    def test_reverse(self):
        result = StringManipulator('goodbye', Reverse()).process_string()
        self.assertEqual('eybdoog', result)

    def test_every_other(self):
        result = StringManipulator('hello', EveryOther()).process_string()
        self.assertEqual('hlo', result)
    
    def test_to_list(self):
        result = StringManipulator('bob', ToList()).process_string()
        self.assertEqual(['bob'], result)
