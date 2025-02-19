# Example usage
from calc_proj.Calculator import Calculator

def main():
    calc = Calculator()

    # Basic operations
    result1 = calc.add(5, 3)        # 8.0
    print(f"Addition result: {result1}")
    result2 = calc.subtract(10, 4)   # 6.0
    print(f"Subtraction result: {result2}")
    result3 = calc.multiply(2, 3)    # 6.0
    print(f"Multiplication result: {result3}")
    result4 = calc.divide(10, 2)     # 5.0
    print(f"Division result: {result4}")
    result5 = calc.power(2, 3)       # 8.0
    print(f"Power result: {result5}")

    # Get last result
    last_result = calc.get_last_result()  # 8.0

    # Clear last result
    calc.clear_last_result()
