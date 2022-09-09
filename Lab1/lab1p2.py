import math                     # makes the math function available
from math import pi				# makes the pi available

###
### Problem 2
### Write a Python program which accepts the radius of a circle 
### from the user and compute the area then print the it out. 
### Sample Output :
### r = 1.1
### Area = 3.8013271108436504

print ("Problem 2 solution follows:")
r = float(input ("Input the radius of the circle : ")) # Takes a float as an input of radius

#Let's create a function to do this.

def circle_area(radius):
    """Calculate the area of the circle
        
        INPUT:
        Radius
        
        OUTPUT:
        Area = PI * r**"""
    return 3.14 * radius**2

print(f"\tArea: {circle_area(r)}")
