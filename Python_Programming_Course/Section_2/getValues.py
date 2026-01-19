# Use input function to get user input, it will be always a string
name = input("Please enter your name: ")

# There are multiples ways to show the value of a variable
print("Hello, " + name)  # Using print function with concatenation
print(f"Hello, {name}")        # Using f-string for formatted output ---> This is the best way
print("Hello, {}".format(name)) # Using format method
print("Hello,", name)     # Using print function with comma separation

# If you want to get a number from user input, you need to convert it
age_str = input("Please enter your age: ")
age = int(age_str)  # Convert string to integer
# Or you can do it in one line --> age = int(input("Please enter your age: "))
print(f"You are {age} years old.")
