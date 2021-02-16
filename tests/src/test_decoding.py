#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from src.decoding import decoding_func
from src.cipher import select_alphabet

alphabet = select_alphabet("w")
key = 2


# Test cases to test 'encoding' methods
class TestEncode(unittest.TestCase):
    def test_decoding(self):
        self.assertEqual(decoding_func("y", alphabet, key), "w")
        self.assertEqual(decoding_func("c", alphabet, key), "a")

    def test_value(self):
        self.assertRaises(ValueError, decoding_func, "й", alphabet, key)
        self.assertRaises(ValueError, decoding_func, "я", alphabet, key)

    def test_type(self):
        self.assertRaises(TypeError, decoding_func, 1, alphabet, key)


if __name__ == "__main__":
    unittest.main()
