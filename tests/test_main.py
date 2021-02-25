#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import main
import os


# Test cases to test 'encoding' methods
class TestMain(unittest.TestCase):
    def test_main(self):
        result = os.system("python main.py")
        self.assertEqual(result, 2)
        # now check that the script's output is what you expect
