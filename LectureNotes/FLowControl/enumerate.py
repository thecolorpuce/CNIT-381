"""
Enumerate

enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.
"""

letters = ['a', 'b', 'c', 'd', 'e']

for i, letter in enumerate(letters):
    print(i, letter)