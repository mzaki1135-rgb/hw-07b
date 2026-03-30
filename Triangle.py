# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    # Check for invalid inputs
    if not all(isinstance(x, int) for x in [a, b, c]):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check triangle inequality
    if a + b <= c or b + c <= a or c + a <= b:
        return 'NotATriangle'

    # Check for right triangle
    if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
        return 'Right'

    # Check triangle type
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isoceles'
    else:
        return 'Scalene'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
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
