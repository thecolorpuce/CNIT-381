"""
zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)].

Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

You could unpack each tuple in a for loop like this.
"""

letters = ['a', 'b', 'c']
nums = [1, 2, 3]
some_list = []

#This is zipping two lists together

for letter, num in zip(letters, nums):
    print(f"{letter}: {num}")

#Unzipping 

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

print(letters)
print(nums)
