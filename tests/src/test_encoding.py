#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from src.encoding import encoding_func
from src.select_alphabet import select_alphabet

alphabet = select_alphabet("w")
key = 2


# Test cases to test 'encoding' methods
class TestEncode(unittest.TestCase):
    # Expected Result Test
    def test_decoding(self):
        self.assertEqual(encoding_func("w", alphabet, key), "y")
        self.assertEqual(encoding_func("a", alphabet, key), "c")

    # Checking for an invalid value
    def test_value(self):
        self.assertRaises(ValueError, encoding_func, "й", alphabet, key)
        self.assertRaises(ValueError, encoding_func, "я", alphabet, key)

    # Checking for the wrong input data type
    def test_type(self):
        self.assertRaises(TypeError, encoding_func, 1, alphabet, key)


if __name__ == "__main__":
    unittest.main()
