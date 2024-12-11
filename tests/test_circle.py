import unittest as ut
import math
import sys
sys.path.append("..")

from circle import area, perimeter

class TestCircle(ut.TestCase):

    def test_area_basic(self):
        r = 1
        expected_result = math.pi
        self.assertAlmostEqual(area(r), expected_result, delta=1e-6)


    def test_area_radius_zero(self):
        r = 0
        expected_result = 0
        self.assertAlmostEqual(area(r), expected_result, delta=1e-6)
        
        
    def test_area_radius_negative(self):
        r = -1
        with self.assertRaises(TypeError):
            area(r)
            
            
    def test_perimeter_basic(self):
        r = 1
        expected_result = 2 * math.pi
        self.assertAlmostEqual(perimeter(r), expected_result, delta=1e-6)


    def test_perimeter_radius_zero(self):
        r = 0
        expected_result = 0
        self.assertAlmostEqual(area(r), expected_result, delta=1e-6)
        
        
    def test_perimeter_radius_negative(self):
        r = -1
        with self.assertRaises(TypeError):
            area(r)