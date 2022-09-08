"""
Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.
Python’s “with open(…) as …” Pattern (Links to an external site.)

Reading and writing data to files using Python is pretty straightforward. To do this, you must first open files in the appropriate mode. Here’s an example of how to use Python’s “with open(…) as …” pattern to open a text file and read its contents:
"""
#This writes to the data.txt file. This overwrites existing content
#Specifying the 'w' opens the file in write mode
with open('data.txt', 'w') as f:
    data = 'some data to be written to this file 2.'
    f.write(data)


#Specifying 'r' opens the file in read-only mode
with open('data.txt', 'r') as f:
    data = f.read()
    print(data)