import unittest as ut
import sys
sys.path.append("..")

from square import area, perimeter

class TestSquare(ut.TestCase):
    
    def test_area_basic(self):
        self.assertEqual(area(3), 9)
    
    
    def test_area_negative(self):
        with self.assertRaises(TypeError):
            area(-1)
    
    
    def test_area_zero(self):
        with self.assertRaises(TypeError):
            area(0)
    
    
    def test_perimeter_basic(self):
        self.assertEqual(perimeter(4), 16)
    
    
    def test_perimeter_negative(self):
        with self.assertRaises(TypeError):
            perimeter(-1)
            
    
    def test_perimeter_zero(self):
        with self.assertRaises(TypeError):
            perimeter(0)
            