while True:
    try:
        num_1 = float(input("Enter a Number: "))
        operation = input("Enter Operation: +, -, *, / and q for Quit ")
        if operation == "q":
            break
        num_2 = float(input("Enter second number"))
        if operation == "+":
            print(f"Result: {num_1 + num_2}")
        elif operation == "-":
            print(f"Result: {num_1 - num_2}")
        elif operation == "*":
            print(f"Result: {num_1 * num_2}")
        elif operation == "/":
            if num_2 == 0:
                print("Invalid Number: cannot divide by zero")
            else:
                print(f"Result: {num_1 / num_2}")
        else:
            print('Invalid Operation')
    except ValueError:
        print('Error: Please Enter a Valid Number')