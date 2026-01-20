# That how we get a "list" of odd numbers from 1 to 20 using a generator
def oddNumbers():
    for num in range(1, 21, 2):
        yield num # yield functions as an iterator
        # return num -> Dont use return in generators, it will stop the iteration and get and error
        
# Calling the generator and print the odd numbers one by one
for odd in oddNumbers():
    print(odd)
    
# If we want to get one value at a time, we can use the next() function
odd_gen = oddNumbers() # Create a generator object
print(next(odd_gen)) # Output: 1 -> The iterator move to the next value for ever in the object odd_gen
print(next(odd_gen)) # Output: 3        