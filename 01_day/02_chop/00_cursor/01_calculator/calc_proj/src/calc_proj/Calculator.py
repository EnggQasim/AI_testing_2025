from typing import Union, Optional

class Calculator:
    def __init__(self) -> None:
        self.last_result: Optional[float] = None
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers together."""
        self.last_result = float(a + b)
        return self.last_result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract b from a."""
        self.last_result = float(a - b)
        return self.last_result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers."""
        self.last_result = float(a * b)
        return self.last_result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.last_result = float(a / b)
        return self.last_result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Raise base to the power of exponent."""
        self.last_result = float(base ** exponent)
        return self.last_result
    
    def get_last_result(self) -> Optional[float]:
        """Return the last calculated result."""
        return self.last_result
    
    def clear_last_result(self) -> None:
        """Clear the last result."""
        self.last_result = None
