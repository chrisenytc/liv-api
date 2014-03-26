# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import unittest


class TestLiv(unittest.TestCase):

    def setUp(self):
        self.test = "Welcome to Liv"

    def test_returns_a_hello_world(self):
        self.assertEqual(self.test, 'Welcome to Liv')

if __name__ == '__main__':
    unittest.main()
