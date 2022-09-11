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

