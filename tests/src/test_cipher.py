#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import unittest
from src.cipher import get_input, select_alphabet


# Test cases to test 'encoding' methods
class TestCipher(unittest.TestCase):
    def test_get_input(self):
        pass

    def test_select_alphabet(self):
        self.assertRaises(TypeError, select_alphabet, 1)


if __name__ == "__main__":
    unittest.main()
