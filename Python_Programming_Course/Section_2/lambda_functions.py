# Lambda Fuctions
list = [1,2,3,4,5,6,7,8,9,10]
print(list(map((lambda value: value * value), list))) # map applies a function to a list. In this case, the function has no name and is declared at that moment (a lambda)

# Function Filter
print(list(filter(lambda value: value%2==0), list)) # Similar to the one above, but applying a condition

#Function Reduce
import functools

print(str(functools.reduce(lambda x, resultado: x+resultado), list))