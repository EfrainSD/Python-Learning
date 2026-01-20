import time

# A decorator is a function that takes another function as an argument, extends its behavior without explicitly modifying it
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # args save all positional arguments -> ejemplo(1, 2, 3) -> args save (1, 2, 3)
        # kwargs saves all keyword arguments with names args -> ejemplo(a=1, b=2) -> kwargs save {'a': 1, 'b': 2}
        initTime = time.time() # Here you do thing before calling the original function
        result = original_function(*args, **kwargs) # Call the original function
        endTime = time.time() # Here you do thing after calling the original function
        print(f"Function {original_function.__name__} executed in {round(endTime,2) - round(initTime,2)}")
    return wrapper_function

@decorator_function # Using the decorator to enhance the example_function with additional functionality
def example_function(delay_time): # This is a normal function
    """A simple function that sleeps for a given amount of time."""
    time.sleep(delay_time)
    print(f"Slept for {delay_time} seconds")

example_function(2)  # This will print the sleep message and the execution time

# You can use decorator for validation
def validate_positive_numbers(original_function):
    def wrapper_function(*args, **kwargs):
        for arg in args: # Validate all positional arguments from the original function
            if not isinstance(arg, int): # Check if the argument is an integer
                raise ValueError("All arguments must be positive numbers")
        return original_function(*args, **kwargs) # Call the original function if validation passes
    return wrapper_function

@validate_positive_numbers
def add_positive_numbers(a, b):
    return a + b

print(add_positive_numbers(5, 10))  # Output: 15
# print(add_positive_numbers(-5, 10))  # This will raise a ValueError

# Another example of decorator for user authentication
def authenticate_user(original_function):
    def wrapper_function(*args, **kwargs):
        if not args[0].get("is_authenticated", False):
            raise PermissionError("User is not authenticated")
        return original_function(*args, **kwargs)
    return wrapper_function

user = {"username": "john_doe", "is_authenticated": True}

@authenticate_user
def access_sensitive_data(user):
    return "Sensitive Data Accessed"

print(access_sensitive_data(user))
# user = {"username": "john_doe", "is_authenticated": False}
# print(access_sensitive_data(user)) # This will raise a PermissionError