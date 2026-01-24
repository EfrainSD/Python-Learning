def ask_options():
    print("What do you want to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    option = int(input("Choose an option (1-5): "))
    return option

def calculate(option):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if option == 1:
        print("The result is: ", num1 + num2)
    elif option == 2:
        print("The result is: ", num1 - num2)
    elif option == 3:
        print("The result is: ", num1 * num2)
    elif option == 4:
        if num2 != 0:
            print("The result is: ", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    print("/n/n")

while (option >= 1 and option <= 4):
    calculate(option)
    option = ask_options()
    
print("Exiting the calculator. Goodbye!")