def calculator():
    print("Welcome to the calculator")
    print("You have to enter a choice +,-,*,/")
    choice = input("Enter your choice: ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == "+":
        print(num1 + num2)
    elif choice == "-":
        print(num1 - num2)
    elif choice == "*":
        print(num1 * num2)
    elif choice == "/":
        if num2 != 0:
            print("Result: ", num1 / num2)
        else:
            print("No you can't divide by zero")
    else:
        print("Invalid choice")


calculator()
