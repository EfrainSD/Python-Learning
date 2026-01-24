# list = [expresion for element in secuencia]

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)] # we could also use a list like [0,1,2,3,4,5,6,7,8,9]
print(squares)

# Another example of list comprehension to create a list of even numbers
nums = [1,2,3,4,5,6,7,8,9,10]
evenList = [num % 2 == 0 for num in nums] # ERROR: This will create a list of boolean values where each element indicates if the number is even
# If we want to create a list of even numbers, we should use:
evenList = [num for num in nums if num % 2 == 0]
print(evenList)

# Example of using list comprehension with strings to create a list of uppercase names
names = ["alice", "bob", "charlie"]
upperNames = [name.upper() for name in names]
print(upperNames)

# Another example using strings and comprehesion lists
frase = 'This is a sample sentence'
vocals = [letra for letra in frase if letra.lower() in 'aeiou']
print(vocals)