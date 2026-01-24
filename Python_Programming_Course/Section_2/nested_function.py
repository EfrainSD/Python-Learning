# Example of a nested function -> A function thats contained within another function
def calculator(num1, num2, operation='sumar'):
    # First we define the nested functions for each operation
    def add(num1, num2): return num1 + num2 
    def subtract(num1, num2): return num1 - num2
    def multiply(num1, num2): return num1 * num2
    def divide(num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    
    # Then call the appropriate nested function based on the operation
    if operation == 'sumar':
        print (f"The result of adding {num1} and {num2} is: {add(num1, num2)}")
    elif operation == 'restar':
        print (f"The result of subtracting {num2} from {num1} is: {subtract(num1, num2)}")
    elif operation == 'multiplicar':
        print (f"The result of multiplying {num1} and {num2} is: {multiply(num1, num2)}")
    elif operation == 'dividir':
        print (f"The result of dividing {num1} by {num2} is: {divide(num1, num2)}")
        
    return "Operation completed"
        
print("Calculator with nested functions: ", calculator(10, 5, 'sumar'))