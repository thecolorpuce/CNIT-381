"""
This is version 1 of Lab-01

Will be working on this after my useless elective required for graduation
"""

# Name: Riley Asp
# CNIT-381 - section 002
# Lab 01

# You may do your work by editing this file, or by typing code at
# https://www.programiz.com/python-programming/online-compiler/ to 
# check for result and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.
# Save this file with name in this format: cnit381_1_hw1_YOURNAME
# Submit this file to Stout's Canvas

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


###
### Problem 3
### Write a Python program to display the first and last 
### colors from the following list.
color_list = ["Red","Green","White" ,"Black","Blue","Yellow"]

print ("Problem 3 solution follows:")

#I don't think this needs to be elegant...

print(f"First on the list: {color_list[0]}")    #Index 0 is the first item
print(f"Last on the list {color_list[-1]}")     #Index -1 is always the last item (Unless it isn't because I'm stupid)

###
### Problem 4
### Use list indexing to determine how many days are in a particular month 
### based on the integer variable month, and store that value in the integer 
### variable num_days. For example, if month is 8, num_days should be set to 31, 
### since the eighth month, August, has 31 days.
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
month = 5

print ("Problem 4 solution follows:")

#I am interpreting this as making use of the integer provided in month (5) to be used for the index in 'days_in_month'

num_days = days_in_month[month]

print(num_days)

###
### Problem 5
### Select the three most recent dates from this list using list slicing notation.
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
'March 9, 2016']

print ("Problem 5 solution follows:")

#The three most recent dates
#Nice that they're in order

recent_dates = eclipse_dates[-3 : None] #starting at index -3 (3rd from last) and ending with 'None' as index -1 will ber Mar 20, 2015

print(eclipse_dates)
print("The 3 most recent days are as follows:")
for e in recent_dates:
    print(f"\t{e}")

###
### Problem 6
### print the maximum and minimum lenght of these lists by using len(), max(), min()
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print ("Problem 6 solution follows:")

print("List a:")
print(f"\tMax = {max(a)}, Min = {min(a)}, Len = {len(a)}")
print("\nList b:")
print(f"\tMax = {max(b)}, Min = {min(b)}, Len = {len(b)}")
print("\nList c:")
print(f"\tMax = {max(c)}, Min = {min(c)}, Len = {len(c)}")

# sample output: Max = 4, Min = 2

###
### Problem 7
### Given a list: names = ["Carol", "Albert", "Ben", "Donna"]
### use join() and sorted() to get this output: 
### Albert & Ben & Carol & Donna
names = ["Carol", "Albert", "Ben", "Donna"]

print ("Problem 7 solution follows:")

#The objective is to join this list with '&' and have it in alphabetical order

#Sort alphabetically 
sortedNames = sorted(names)

#Join with '&'
joinedNames = " & ".join(sortedNames)

#Print the names
print(joinedNames)

###
### Problem 8
### Given a list: names = ["Carol", "Albert", "Ben", "Donna"]
### use append() to get this output: 
### ["Carol", "Albert", "Ben", "Donna", "Eugenia"]
names = ["Carol", "Albert", "Ben", "Donna"]
print ("Problem 8 solution follows:")

#Just appending the name 'Eugenia'

names.append('Eugenia')

print(names)

###
### Problem 9
### Define a Dictionary, population,that provides information on 
### the world's largest cities and print it out. The key is the name of a city
### a string), and the associated value is its population in
### millions of people.
###   Key     |   Value
### Shanghai  |   17.8
### Istanbul  |   13.3
### Karachi   |   13.0
### Mumbai    |   12.5

print ("Problem 9 solution follows:")

#Create the dictionary. Using provided examples...

cities = {'Shanghai': 17.8,
        'Istanbul': 13.3,
        'Kerachi': 13.0,
        'Mumbai': 12.5,
        }

#Use a for loop to itterate through the dictionary, and print the key & value.

for k, v in cities.items(): #Using the items method for keys and values
    print(f"City: {k.title()} || Population: {v} million.")

###
### Problem 10
### Run the code below and explain the outcome
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)

"""
print(a == b): True..
It is established that b is == a. They are the same list, so the output is 'True

print(a is b): True..
'is' is used to determine if variables are the same. In this case they are, so it returns true

print(a == c): True..
a && c have the same values, so they are equal..

print(a is c): False..

This is different because b was explicitly defined to be equal to a. c on the other hand just happens to have the same value.
In essence, they are not the same object.
"""