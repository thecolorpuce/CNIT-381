###
### Problem 4
### Use list indexing to determine how many days are in a particular month 
### based on the integer variable month, and store that value in the integer 
### variable num_days. For example, if month is 8, num_days should be set to 31, 
### since the eighth month, August, has 31 days.
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
month = 5

print ("Problem 4 solution follows:")

#I am interpreting this as making use of the integer provided in month (5) to be used for the index in 'days_in_month'

num_days = days_in_month[month]

print(num_days)

