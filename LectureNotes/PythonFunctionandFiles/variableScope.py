"""
Variable Scope

Variable scope refers to which parts of a program a variable can be referenced, or used, from.

It's important to consider scope when using variables in functions. If a variable is created inside a function, it can only be used within that function. Accessing it outside that function is not possible.
"""

#Below is an example of a function that will result in error

"""
def some_function():
    word = "hello"

print(word)
"""

#This is an error as the 'word' variable is local to the 'some_function' scope.

#Doing it this way will work better

def some_function():
    word = "hello"
    print(word)

def another_function():
    word = "goodbye"
    print(word)


some_function()
another_function()

#You can also make use of a globally defined variable
#IE I defined the variable outside of a function