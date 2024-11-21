# Task 1 tests
import unittest
from symtable import Class

from convert import str_to_float


class TestCases(unittest.TestCase):

    def test_str_to_float_1(self):
        input = '5.76'
        result = str_to_float(input)
        expected = 5.76
        self.assertEqual(result, expected)

    def test_str_to_float_2(self):
        input = 'HAMBURGER!'
        result = str_to_float(input)
        expected = None
        self.assertEqual(result, expected)
