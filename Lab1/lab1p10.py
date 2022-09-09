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