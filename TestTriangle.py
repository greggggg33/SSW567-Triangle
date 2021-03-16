# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidTrianglesA(self):
        self.assertEqual(classify_triangle(1,3,5),'NotATriangle','1,3,5 is not a Triangle')
    def testInvalidTrianglesB(self):
        self.assertEqual(classify_triangle(1,201,5),'InvalidInput','1,201,5 is InvalidInput')
    def testInvalidTrianglesC(self):
        self.assertEqual(classify_triangle(45,45,100),'NotATriangle','45,45,100 is not a Triangle')
    def testInvalidTrianglesD(self):
        self.assertEqual(classify_triangle(-5,2,3),'InvalidInput','-5,2,3 is InvalidInput')
    def testInvalidTrianglesE(self):
        self.assertEqual(classify_triangle(-55,-25,-35),'InvalidInput','-55,-25,-35 is InvalidInput')
    def testInvalidTrianglesF(self):
        self.assertEqual(classify_triangle('two','three','one'),'InvalidInput','two,three,one is InvalidInput')

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(5,12,13),'Right','5,12,13 is a Right triangle')
    def testRightTriangleD(self): 
        self.assertEqual(classify_triangle(8,15,17),'Right','8,15,17 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classify_triangle(5,5,5),'Equilateral','5,5,5 should be equilateral')
    def testEquilateralTrianglesC(self): 
        self.assertEqual(classify_triangle(10,10,10),'Equilateral','10,10,10 should be equilateral')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 should be Scalene')
    def testScaleneTrianglesB(self): 
        self.assertEqual(classify_triangle(10,11,12),'Scalene','10,11,12 should be Scalene')

    def testIsocelesTrianglesA(self): 
        self.assertEqual(classify_triangle(2,3,3),'Isoceles','2,3,3 should be Isoceles')
    def testIsocelesTrianglesB(self): 
        self.assertEqual(classify_triangle(15,20,15),'Isoceles','15,20,15 should be Isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

