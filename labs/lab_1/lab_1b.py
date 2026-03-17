"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

#function asks for a type of input and cleans the input to only enter valid data types
def cleanInput(type, message):
    
    looking = True
    #main loop that only ends when a valid value is entered
    while looking:
        #try to make sure good inputs are got
        try:
            if type == "float":
                output = float(input(message))
                looking = False
            #handles operation
            elif type == "operation":
                output = input(message).strip().lower()
                print(output)
                #checks if it is a valid operator
                if output in ["add","subtract","multiply","divide"]:
                    looking = False
                else:
                    print("enter a vaid operator")
        #execpt if a error is thrown
        except:
            print("please enter a valid value!")
    return output

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input  
    num1 = cleanInput("float","Enter the first number: ")
    num2 = cleanInput("float","Enter the second number: ")
    operation = cleanInput("operation", "Enter the operation (add, subtract, multiply, divide): ")
    print(operation)

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
