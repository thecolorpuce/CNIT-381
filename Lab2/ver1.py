# Name: ...
# CNIT-381 Sec...
# Lab-02

# You may do your work by editing this file, or by typing code at
# https://www.programiz.com/python-programming/online-compiler/ to 
# check for result and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.
# Save this file with name in this format: cnit381_1_hw2_YOURNAME
# Submit this file to Stout's Canvas


###
### Problem 1 (20 points)
### Is Unique: Implement an algorithm to determine if a string has all unique characters. 
### Sample Output:
### "abcdefg" is Unique 
### "abcdebg" is not

print ("Problem 1 solution follows:")
input = input("Input a string: ")# Takes a string as an input

#I think I could itterate through the string, and make a counter for each character in the string

def unique(st):
    #I'm stupid. The best method I can figure is to make use of two for loops
    #loop 'v' steps into a second for loop 'j'
    #Essentially we start at the first position with the first for loop.
    #Then we loop through the string
    #If the same value is found, we return false
    #If no values are foun, we return True
    for v in range(0, len(st)):
        for j in range(v + 1, len(st)): #+1 to avoid counting the current value
            if(st[v] == st[j]):
                return False
    return True                         #We return true after the whole loop has itterated


print(unique(input))    #Call the function, and go forth.

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
nums = input ("Input: ") # Takes a list of int
# ... write your code and comments here (and remove this line)


###
### Problem 3 (10 points)
### Given a list of integers, a lucky integer is an integer which has a frequency 
### in the list equal to its value.
### Return a lucky integer in the list. If there is no lucky integer return -1.
###
### Example 1:
### Input: [2,2,3,4]
### Output: 2
### Explanation: The only lucky number in the list is 2 because frequency[2] == 2.
###
### Example 2:
### Input: [1,2,2,3,3,3]
### Output: 3
### Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
###
### Example 3:
### Input: [2,2,2,3,3]
### Output: -1
### Explanation: There are no lucky numbers in the list.
nums1 = [2,2,3,4]
nums2 = [1,2,2,3,3,3]
nums3 = [2,2,2,3,3]
print ("Problem 3 solution follows:")
# ... write your code and comments here (and remove this line)

###
### Problem 4 (20 points)
### The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
### such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
### F(0) = 0,   F(1) = 1
### F(N) = F(N - 1) + F(N - 2), for N > 1.
### Given N, calculate F(N). 
###
### Example 1:
### Input: 2
### Output: 1
### Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
###
### Example 2:
### Input: 3
### Output: 2
### Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
###
### Example 3:
### Input: 4
### Output: 3
### Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
n = input ("Input: ") # Takes a an int
print ("Problem 4 solution follows:")
# ... write your code and comments here (and remove this line)


###
### Problem 5 (30 points)
### Sorted Merge: You are given two sorted integer lists, A and B, where A has a large enough 
### buffer at the end to hold B. Write a function to merge B into A in sorted order.
###
### Example:
### A = [1,3,4,8,9]
### B = [2,4,5,6,7]
### output [1,2,3,4,4,5,6,7,8,9]

print ("Problem 5 solution follows:")
# ... write your code and comments here (and remove this line)
