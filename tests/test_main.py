#!/usr/bin/python
# -*- coding: UTF-8 -*-

import main
import os
import unittest


# Test cases to test 'main.py' file
class TestMain(unittest.TestCase):
    # check that the script output matches your expectations
    def test_main_encode(self):
        result = os.system("python main.py e abc")
        self.assertEqual(result, 0)

    # check that the script output matches your expectations
    def test_main_decode(self):
        result = os.system("python main.py d abc")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
