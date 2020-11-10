"""
Created on Tue Nov 10 12:44:14 2020

@author: Dominik Euba
"""

def area (h, b):
    return (h*b) / 2

#print to console 
print("this application calculates the area of a triangle:")

#user input for height and side length
h =  float(input('enter height of the triangle in cm: '))
b =  float(input('enter base side of the triangle in cm: '))

#calculating area of the triangle
trianglearea = area(h,b)

#print solution to the console
print("the circle has an area of: " , round(circlearea,2), "cm^2")

