"""
Sets

A set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list.
"""

numbers = [1, 2, 6, 3, 1, 1, 6]

uniqueNums = set(numbers)
print(uniqueNums) 

"""
Sets support the in operator the same as lists do. You can add elements to sets using the add method, and remove elements using the pop method, similar to lists.
Although, when you pop an element from a set, a random element is removed. Remember that sets, unlike lists, are unordered so there is no "last element".
"""

fruit = {'apple', 'banana', 'orange', 'grapefruit'} #Set defined

print("watermelon" in fruit) #Check for element

fruit.add("watermelon") #Add the element
print(fruit)

print(fruit.pop()) #Remove a random element
print(fruit)