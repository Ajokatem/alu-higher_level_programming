#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
from max_integer import max_integer
class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)
    def test_two_element_list(self):
        self.assertEqual(max_integer([1, 2]), 2)
    def test_three_element_list(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_list_with_negative_numbers(self):
        self.assertEqual(max_integer([-1, 2, 3]), 3)
    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([1, 2, 3, 2]), 3)
if __name__ == "__main__":
    unittest.main()
