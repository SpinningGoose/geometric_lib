import unittest as ut
import sys
sys.path.append("..")

from rectangle import area, perimeter

class TestRectangle(ut.TestCase):

    def test_area_args_zero(self):
        self.assertEqual(area(1, 0), 0) 
        self.assertEqual(area(0, 1), 0)
        
    
    def test_area_length_negative(self):
        with self.assertRaises(TypeError):
            area(-1, 1)
            
            
    def test_area_width_negative(self):
        with self.assertRaises(TypeError):
            area(1, -1)
            
    
    def test_area_basic(self):
        self.assertEqual(area(2, 3), 6)
        
        
    def test_perimeter_length_zero(self):
        with self.assertRaises(TypeError):
            perimeter(0, 1)
            
            
    def test_perimeter_width_zero(self):
        with self.assertRaises(TypeError):
            perimeter(1, 0)
            
            
    def test_perimeter_length_negative(self):
        with self.assertRaises(TypeError):
            perimeter(-1, 1)
            
            
    def test_perimeter_width_negative(self):
        with self.assertRaises(TypeError):
            perimeter(1, -1)
            
            
    def test_perimeter_basic(self):
        self.assertEqual(perimeter(2, 4), 12)