import unittest
from circles import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        '''test area when radius >=0'''
        from math import pi
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),2.1**2*pi)
    def test_values(self):
        '''Make sure that value errors raised when necessary'''
        self.assertRaises(ValueError, circle_area, -2)
    def test_types(self):
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, [1,2,3])
        self.assertRaises(TypeError, circle_area, 'number')
