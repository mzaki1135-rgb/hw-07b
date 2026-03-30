# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testScalene(self):
        self.assertEqual(classifyTriangle(3,4,6),'Scalene')

    def testIsosceles(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isosceles')

    def testInvalidZero(self):
        self.assertEqual(classifyTriangle(0,1,2),'InvalidInput')

    def testInvalidNegative(self):
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput')

    def testTooLarge(self):
        self.assertEqual(classifyTriangle(201,2,3),'InvalidInput')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(6,8,10),'Right')

    def testNonInteger(self):
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput')
            def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScalene(self):
        self.assertEqual(classifyTriangle(3,4,6),'Scalene')

    def testIsosceles(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles')

    def testInvalidZero(self):
        self.assertEqual(classifyTriangle(0,1,2),'InvalidInput')

    def testInvalidNegative(self):
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput')

    def testTooLarge(self):
        self.assertEqual(classifyTriangle(201,2,3),'InvalidInput')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(6,8,10),'Right')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

