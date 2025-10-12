from decimal import Decimal, InvalidOperation


def decimal_to_binary(value):
    value = value.strip()
    try:
        if value.endswith('%'):
            num = Decimal(value[:-1]) / 100
        else:
            num = Decimal(value)
        return num
    except InvalidOperation:
        print("❌ Invalid number format:", value)
        return Decimal(0)


def calculator():
    print("Welcome to the calculator")
    num1 = decimal_to_binary(input("Enter the first number: "))
    num2 = decimal_to_binary(input("Enter the second number: "))

    while True:
        print("You have to enter a choice +,-,*,/")
        choice = input("Enter your choice: ")
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
                return ()
        else:
            print("Invalid choice-_-")
        exit()


calculator()
