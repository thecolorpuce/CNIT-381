"""
Join Method

Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
"""

new_str = "\n".join(['fore', 'aft', 'starboard', 'port']) #This example is using '\n' as a separator. Running this shows each item in the list in a new line

print(new_str)

#An example with a name, using a hyphen

print("\n\n")

name = "-".join(["Garcia", "O'Kelly"])

print(name)