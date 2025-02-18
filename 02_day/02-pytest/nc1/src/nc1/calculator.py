def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Args:
        a: The dividend
        b: The divisor
    
    Returns:
        float: The result of the division
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def power(a: float, b: float) -> float:
    """Calculate a raised to the power of b and return the result."""
    return a ** b
