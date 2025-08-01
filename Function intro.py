# Function Definition and Creation
def greet(name):
    """
    This function greets the person passed in as a parameter.
    This is a docstring, explaining what the function does.
    """
    message = f"Hello, {name}!" # Local variable 'message'
    return message # Returns a string

# Function Call
my_name = "Alice" # Global variable 'my_name'
greeting_message = greet(my_name) # Call the function
print(greeting_message)

# Accessing Docstring
print(greet._doc_)

# Variable Lifetime
# 1. Global Variable: 'my_name' exists throughout the script's execution.
# 2. Local Variable: 'message' exists only within the 'greet' function.
#    Once 'greet' finishes, 'message' is destroyed.

# Example of another local variable
def calculate_area(length, width):
    area = length * width # 'area' is local to calculate_area
    return area

result = calculate_area(5, 10)
print(f"Area: {result}")

# Attempting to access a local variable outside its scope will cause an error:
# print(message) # This would raise a NameError because 'message' is not defined here.
