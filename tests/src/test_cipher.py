#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from src.cipher import get_input, select_alphabet


# Test cases to test 'encoding' methods
class TestCipher(unittest.TestCase):
    def test_get_input(self):
        self.assertEqual(get_input(), "")


if __name__ == "__main__":
    unittest.main()
