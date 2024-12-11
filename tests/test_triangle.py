import unittest as ut
import sys
sys.path.append("..")

from triangle import area, perimeter

class TestTriangle(ut.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 5), 0)
        
        
    def test_area_basic(self):
        self.assertEqual(area(3, 2), 3)
        
        
    def test_area_side_negative(self):
        with self.assertRaises(TypeError):
            area(-1, 2)
    
    
    def test_area_height_negative(self):
        with self.assertRaises(TypeError):
            area(2, -1)
            
            
    def test_perimeter_side_zero(self):
        with self.assertRaises(TypeError):
            perimeter(0, 0, 0)
    
    
    def test_perimeter_sides_negative(self):
        with self.assertRaises(TypeError):
            perimeter(-1, -2, -3)
            
    def test_perimeter_basic(self):
        self.assertEqual(perimeter(1, 2, 3), 6)