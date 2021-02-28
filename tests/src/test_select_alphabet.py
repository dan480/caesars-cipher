#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from src.select_alphabet import select_alphabet


# Test cases to test 'select_alphabet' methods
class TestCipher(unittest.TestCase):
    def test_select_alphabet(self):
        self.assertRaises(TypeError, select_alphabet, 1)


if __name__ == "__main__":
    unittest.main()
