```python
def generate_addition_function_code():
    """Generates Python code for a function that adds two numbers."""

    code = """
def add_two_numbers(a: int | float, b: int | float) -> int | float | str:
    """Adds two numbers and returns the sum.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.  Returns an error message if input is not a number.

    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Error: Inputs must be numbers."

#Example usage
print(add_two_numbers(5,3)) # Output: 8
print(add_two_numbers(10.5, 2.5)) #Output: 13.0
print(add_two_numbers("hello", 5)) # Output: Error: Inputs must be numbers.

"""
    return code

# Generate and print the code
generated_code = generate_addition_function_code()
print(generated_code)


# You can also save the generated code to a file if needed:
# with open("addition_function.py", "w") as f:
#     f.write(generated_code)
```