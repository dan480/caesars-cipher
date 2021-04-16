#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from src.decoding import decoding_func
from src.select_alphabet import select_alphabet

alphabet = select_alphabet(r"w")
key = 2


# Test cases to test 'decoding' methods
class TestEncode(unittest.TestCase):
    # Expected Result Test
    def test_decoding(self):
        self.assertEqual(decoding_func("y", alphabet, key), "w")
        self.assertEqual(decoding_func("c", alphabet, key), "a")

    # Checking for an invalid value
    def test_value(self):
        self.assertRaises(ValueError, decoding_func, "й", alphabet, key)
        self.assertRaises(ValueError, decoding_func, "я", alphabet, key)

    # Checking for the wrong input data type
    def test_type(self):
        self.assertRaises(TypeError, decoding_func, 1, alphabet, key)


if __name__ == "__main__":
    unittest.main()
