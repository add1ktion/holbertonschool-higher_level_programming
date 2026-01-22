#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_liste_normale(self):
        self.assertEqual(max_integer([1,2,3,4]), 4)
    
    def test_liste_inverse(self):
        self.assertEqual(max_integer([4,3,2,1]), 4)
    
    def test_liste_unique(self):
        self.assertEqual(max_integer([42]), 42)
    
    def test_liste_identique(self):
        self.assertEqual(max_integer([5,5,5]), 5)
    
    def test_liste_vide(self):
        self.assertIsNone(max_integer([]))
    
    def test_negatifs(self):
        self.assertEqual(max_integer([-1,-5,-2]), -1)
    
    def test_melange(self):
        self.assertEqual(max_integer([0, -1, 10]), 10)

if __name__ == '__main__':
    unittest.main()