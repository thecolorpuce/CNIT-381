###
### Problem 2 (20 points)
### Given a non-empty list of integers, every element appears twice except for one.
### Find that single one.
### Note: Could you implement it without using extra memory?
### Example 1:
### Input: [2,2,1]
### Output: 1
### Example 2:
### Input: [4,1,2,1,2]
### Output: 4

print ("Problem 2 solution follows:")
nums = int(input ("Input: ")) # Takes a list of int || Modified this to require an int

#I am unsure of how to find it without extra memory.
#Perhaps that is something we've yet to go over. I'll just try this in my own way for now.

def unique_nums(nums):

    for i in nums:
        print(i)

print(unique_nums(nums))