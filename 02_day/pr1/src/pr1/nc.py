from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def nc_test_generator(file_path: str) -> None:
    """
    Generate test cases for the nc command.
    """
    with open(file_path, 'r') as file:
        codes = file.read()

    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[
            {"role": "system", "content": "You are a test case generator for the given code."},
            {"role": "user", "content": codes}
        ]
    )
    result = response['choices'][0]['message']['content']
    
    with open('test_cases.py', 'w') as file:
        file.write(result)