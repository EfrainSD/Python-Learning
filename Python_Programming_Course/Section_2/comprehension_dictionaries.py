# dict = {key: value for item in iterable if condition}
num = [1,2,3,4,5,6,7,8,9,10]

# Create a dictionary of numbers and their squares
dict_squares = {x: x**2 for x in num}
print(dict_squares)

# Another example of dictionary comprehension to create a dictionary of even numbers and their squares
even_dict = {x: x**2 for x in num if x % 2 == 0}
print(even_dict)

# Example of using dictionary comprehension with strings to create a dictionary of names and their lengths
names = ["alice", "bob", "charlie"]
name_length = {name: len(name) for name in names}
print(name_length)