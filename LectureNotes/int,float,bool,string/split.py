"""
A helpful string method when working with strings is the .split method. This function or method returns a data container called a list that contains the words from the input string. We will be introducing you to the concept of lists in the next video.

The split method has two additional arguments (sep and maxsplit). The sep argument stands for "separator". It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). If the sep argument is not provided, the default separator is whitespace.

True to its name, the maxsplit argument provides the maximum number of splits. The argument gives maxsplit + 1 number of elements in the new list, with the remaining string being returned as the last element in the list. You can read more about these methods in the Python documentation too.

Here are some examples for the .split() method.
"""

newStr = 'The cow jumped over the moon.'

print(newStr.split())

#Setting the max split to 3

print(newStr.split(' ',3)) #Seperator ' ' is a space

#Using a . as the seperator
print(newStr.split('.'))

#No seperator, but a max split of 3

print(newStr.split(None, 3))