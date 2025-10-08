def calculator():
    """
    Performs basic arithmetic operations based on user input.
    """
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    operation = input("Enter operation choice (1/2/3/4/5): ")

    if operation == '1' or operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2' or operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3' or operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4' or operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    elif operation == '5' or operation == 'exit':
        print("Thanks for using the calculator. Goodbye!")
        return
    else:
        print("Invalid operation choice. Please choose 1, 2, 3, 4, or 5.")

# Run the calculator
calculator()