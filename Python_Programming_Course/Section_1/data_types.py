# This is a sample Python file for a programming course demonstrating basic data types.
print("Start")

print("Integer: ", type(42))

print("Float: ", type(3.14))

print("String: ", type("Hello"))

print("Boolean: ", type(True))

# String concatenation
print("Hello, " + "world!")
print("Hello"*4) # Repeat string 4 times

#Variables
v = "This is a variable"
print(v)
v = "This is a new value " + v
print(v)
print(v[1:10])  # Slicing the string, spaces included, starts at 0
print(v[-1])    # Last character of the string
print(len(v))   # Length of the string, including spaces
print(v.lower()) # Convert to lowercase
print(v.upper()) # Convert to uppercase
print(v.capitalize()) # Capitalize first letter
print(v.replace("new", "old")) # Replace substring but does not change original string
print("          HOLA          ".strip()) # Remove leading and trailing whitespace