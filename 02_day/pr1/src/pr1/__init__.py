from pr1.nc import nc_test_generator
import os


    # nc_test_generator("pr1/users.py")

def fun1() -> None:
    print('Hello from fun1')
    file = str(os.getcwd()) + "/src/pr1/users.py"
    # print(os.path.abspath(__file__))
    nc_test_generator(file)
    
def main() -> None:
    print("Hello from pr1!")
