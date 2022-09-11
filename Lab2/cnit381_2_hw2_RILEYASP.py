# Name: Riley Asp
# CNIT-381 Sec002
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
p1in = input("Input a string: ")# Takes a string as an input

#I think I could itterate through the string, and make a counter for each character in the string

def unique(string):
    #I'm stupid. The best method I can figure is to make use of two for loops
    #loop 'v' steps into a second for loop 'j'
    #Essentially we start at the first position with the first for loop.
    #Then we loop through the string
    #If the same value is found, we return false
    #If no values are foun, we return True
    for i in range(0, len(string)):
        for j in range(i + 1, len(string)):
            if(string[i] == string[j]):
                return "This string is not Unique"            #Return Flase if v&j match
    return "This string is unique"                        #Retrun True if loop completes


print(unique(p1in))    #Call the function, and go forth.


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
nums = input("Input: ") 

#I am unsure of how to find it without extra memory.
#Perhaps that is something we've yet to go over. I'll just try this in my own way for now.

def unique_nums(nums):
    """Find the unique number
    
    INPUT:
    [2,2,1]
    
    OUTPUT:
    1"""

    out = ""
    list = {}                   #A dictionary to store information in. k = the integers provided, v = number of times integer appears
    uniq = []                   #A list to hold the unique values from the 'list' dictionary

    #This for loop is used to populate the list dictionary with the keys and values to help find unique vlaues
    for i in nums:              
        if i not in list:       
            list[i] = 1
        else:
            list[i] += 1
    #for loop that goes through the k,v in the 'list dictionary
    for k, v in list.items():
        if v == 1:
            uniq.append(k)      #If v == 1, then it is a unique value. We append it to the 'uniq' list
        else: 
            continue            #Continue looping if above if statement is not met

    return uniq

print(', '.join(unique_nums(nums))) #This way we can display multiple unique numbers.


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


nums1 = [2,2,3,4,4]
nums2 = [1,2,2,3,3,3]
nums3 = [2,2,2,3,3]
nums4 = [1,3,3,2,6,2]
print ("Problem 3 solution follows:")

def lucky_int(list):
    """Lucky int... Number appears the same number of times as its value. 2 would be lucky if it showed up twice.
        INPUT:
        A list of integers
        
        OUTPUT:
        Lucky Integers"""

#I guess I could do something weird

    c1 = 0
    lucky = {}                   #A dictionary that I use to store the key(value from list) and value(number of times the value appears in the list)
    list.sort()                  #Not relevant in this example, but this will ensure unsorted lists will bring back the largest value

    #I should make a dictionary that holds the key(list) and value (number of times integer appears in the list)
    for i in list:              #A for loop that itterates through the provided list
        if i not in lucky:      #if the integer is not in the 'lucky' dictionary, we add it, and assign it a value of 1
            lucky[i] = 1
        else:
            lucky[i] += 1       #If the value already exists, we increment the value of the integer by 1. If we have two 2's, the key value pair would be {2: 2}

    #The dictionary 'lucky' now has associated values. 
    #Ittereate through the dictionary, and find the largest value that is lucky
    for k, v in lucky.items():  #for loop itterating through the dictionary. k(key), v(value)
        if k == v:              #If the key == the value, we assign the variable c1 to = k
            c1 = k              #this is overwritten when a new value enters the scope. Since this is sorted, that value will be larger
        else:
            continue            #If k != v, we continue looping
    
    if c1 == 0:                 #Requirements wanted to return a -1 instead of a 0
        return -1
    return c1



#This is close. I'll come back to it in a bit


print(f"\n{lucky_int(nums1)}")
print(f"\n{lucky_int(nums2)}")
print(f"\n{lucky_int(nums3)}")
print(f"\n{lucky_int(nums4)}")  #My extra example list nums4 working as intended

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

n = int(input ("Input: ")) # Takes a an int
print ("Problem 4 solution follows:")

#Let's make a function that performs the Fibonacci sequence

#Formulat provided above F(N) = F(N - 1) + F(N - 2), for N > 1.

def fibonacci(num):
    """The Fibonacci sequence
    F(N) = F(N - 1) + F(N - 2), for N > 1
    
    INPUT:
    An integer. 
    
    OUTPUT:
    previousFib = 0
    newFib = 1
    currentFib
    if num = 3

    loop 3-1 (2):
        newFib = pf(0) + cf(1)
        previousFib = cf(1)
        currentFib = nf(1)
        ---
    loop:
        newFib = pf(1) + cf(1)
        previousFib = cf(1)
        currentFib = nf(2)

    return currentFib (2)"""
    
    if num <= 1:
        return num                          #Simply retrun the value of 'num' if it is <= 1
    
    pF = 0                                  #We start with 0 & 1
    cF = 1

    for i in range(num - 1):                #We need to itterate through. So, we create a for loop that is 1 less than the value provided
        nF = pF + cF                        #new Fib is eaual to 0 + 1 (For the first pass)
        pF = cF                             #previous Fib takes the value of currentFib (previousFib = 1 (first pass)) 
        cF = nF                             #currentFib takes the value of newFib (1 on the first pass)
    
    return cF                               #Return the value of currentFib after the for loop is done



print(f"\nF({n}) = {fibonacci(n)}")


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

#A sorted buffer. I think we could make use of the zip function for this
#I'll make use of the two provided lists above

A = [1,3,4,8,9]
B = [2,4,5,6,7]

def sortedMerge(a, b):
    """Sorted Merge
    We're trying to numerically sort two lists
    
    INPUT:
    Two equal length lists of numerics
    
    OUTPUT:
    The contents of the two lists merged into one list, and sorted numerically"""
    
    for i in b:
        output = i
        a.append(output)
    
    a.sort()
    return a

A = sortedMerge(A, B)       #Call the function, and print

print(A)
#This feels too simple, but to my understanding, it works. So here we are