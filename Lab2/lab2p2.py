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
nums = input ("Input: ") # Takes a list of int || Modified this to require an int

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