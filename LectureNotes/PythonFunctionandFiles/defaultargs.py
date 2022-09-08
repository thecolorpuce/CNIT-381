#You can make use of default arguments for a function.

def cylinder_volume(height, radius=5):  #Here we have a default radius of 5
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10))  #Now we only need one argument for the function

#However, you can still perform two arguments

print(cylinder_volume(5, 5))