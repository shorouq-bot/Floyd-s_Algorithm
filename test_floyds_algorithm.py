# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:05:12 2024

@author: lenovo
"""

import unittest
import sys
NO_PATH=sys.maxsize
from floyds_algorithm import floyd, floyd_recursive

class TestFloydsAlgorithm(unittest.TestCase):
    def test_floyd_recursive(self):
        # Test case 1
        graph1 = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        self.assertEqual(floyd_recursive(graph1, 0, 3, 2), 8)

        # Test case 2
        graph2 = [
            [0, 5,NO_PATH, 10],
            [NO_PATH, 0, 3, NO_PATH],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        self.assertEqual(floyd_recursive(graph2, 1, 3, 2), NO_PATH)  # No path exists

    def test_floyd(self):
        # Test case 1
        graph1 = [
            [0, 5, NO_PATH, 10],
            [NO_PATH, 0, 3, NO_PATH],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        expected_result1 = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0,2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        self.assertEqual(floyd(graph1), expected_result1)

        # Test case 2
        graph2 = [
            [0, 5, NO_PATH, 10],
            [NO_PATH, 0, 3,NO_PATH],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        expected_result2 = [
            [0, 5, 8, 9],
            [NO_PATH, 0, 3, 4],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        self.assertEqual(floyd(graph2), expected_result2)

if __name__ == '__main__':
    unittest.main()
