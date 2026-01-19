# ------------------------------- IF -------------------------------
x = 10
if x > 5: # You can use it with () but it's not necessary
    print("x is greater than 5")
    pass # You can use pass as a placeholder for future code
elif x == 5:
    print("x is equal to 5")
else:
    print("x is not greater than 5")
    
    
# ------------------------------- WHILE ----------------------------
tabla = int(input("Enter a number to display its multiplication table: "))
count = 1
while (count <= 10): # You can use it with () but it's not necessary
    result = tabla * count
    print(f"{tabla} x {count} = {result}") # Using f-string for formatted output
    count += 1 # If you forget this line, it will create an infinite loop
    # To avoid infinite loops, you can use a break statement
    if count > 10:
        break


# ------------------------------- FOR ------------------------------
tabla = int(input("Enter a number to display its multiplication table: "))
count = 1
for count in range(1, 11): # range(start, end) end is EXCLUSIVE
    result = tabla * count
    print(f"{tabla} x {count} = {result}")
    
# For with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    # You can combine for with if
    if fruit == "banana":
        print("Yellow fruit found!")
        # If you want to stop the loop when a condition is met, use break
    
        
# ------------------------------- DEF ------------------------------
def greet_user(name):
    """Function to greet a user by name.""" # To describe the function
    print(f"Hello, {name}!")
greet_user("Alice")

# You can have functions with return values
def add_numbers(a, b):
    """Function to add two numbers and return the result."""
    return a + b
result = add_numbers(5, 3)
print(f"The sum is: {result}")