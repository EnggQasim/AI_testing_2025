import functools
import pytest
import json
from typing import Callable, Any
import os
from typing import Dict, List

# Store for generated test functions
TEST_FUNCTIONS: Dict[str, List[Callable]] = {}

def test_generator(file_path: str) -> Callable:
    """
    Decorator that generates 5 pytest cases for a function using test cases from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing test cases
        
    Returns:
        Callable: Decorated function with generated test cases
    """
    def decorator(func: Callable) -> Callable:
        # Get absolute path for the test file
        abs_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
        
        # Read test cases from JSON file
        if not os.path.exists(abs_file_path):
            raise FileNotFoundError(f"Test case file not found: {abs_file_path}")
        
        with open(abs_file_path, 'r') as f:
            test_cases = json.load(f)
        
        # Generate test functions
        test_list = []
        for i in range(5):
            test_case = test_cases[i] if i < len(test_cases) else None
            
            def make_test(tc=test_case, idx=i):
                def test():
                    if tc is None:
                        pytest.skip("No test case available")
                    
                    # Extract input and expected output from test case
                    input_data = tc.get('input', {})
                    expected_output = tc.get('expected_output')
                    
                    # Run the actual function with test inputs
                    result = func(**input_data)
                    
                    # Assert the result matches expected output
                    assert result == expected_output, \
                        f"Test case {idx+1} failed: expected {expected_output}, got {result}"
                
                return test
            
            test_func = make_test()
            test_func.__name__ = f"test_{func.__name__}_{i+1}"
            test_func = pytest.mark.generated(test_func)
            test_list.append(test_func)
        
        # Store the generated tests
        TEST_FUNCTIONS[func.__name__] = test_list
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# Create test functions in module scope
def pytest_generate_tests(metafunc):
    """Pytest hook to generate tests."""
    for func_name, tests in TEST_FUNCTIONS.items():
        for test in tests:
            globals()[test.__name__] = test

@test_generator("login_tests.json")
def login(username: str, password: str) -> bool:
    """
    Static login function that checks for admin credentials.
    
    Args:
        username (str): The username to check
        password (str): The password to check
        
    Returns:
        bool: True if credentials match, False otherwise
    """
    return username == "admin" and password == "admin"

@test_generator("signup_tests.json")
def signup(username: str, password: str) -> bool:
    """
    Static signup function that only allows admin credentials.
    
    Args:
        username (str): The username to check
        password (str): The password to check
        
    Returns:
        bool: True if credentials match admin values, False otherwise
    """
    if username == "admin" and password == "admin":
        return True
    return False
