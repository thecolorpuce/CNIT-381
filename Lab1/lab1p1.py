import math                     # makes the math function available
from math import pi				# makes the pi available

###
### Problem 1
### Write a Python program to convert radian to degree.
### Note: The radian is the standard unit of angular measure, used in many 
### areas of mathematics. An angle's measurement in radians is numerically 
### equal to the length of a corresponding arc of a unit circle; one radian is 
### just under 57.3 degrees (when the arc length is equal to the radius).
### Hint: https://www.varsitytutors.com/hotmath/hotmath_help/topics/radian-to-degree-measure
### Sample output:
### Input radians: 10                                                                                             
### 572.7272727272727

print ("Problem 1 solution follows:")
radian = float(input("Input radians: "))# Takes a float as an input of radius



def radian_to_degree(radian):
    """Convert Radians to degrees:
    
        INPUT:
        radian
        
        Output:
        degrees."""
    return radian * 180 / 3.14

print(f"The degrees are {radian_to_degree(radian)}.")