def calculatorsymb():
    text = input("Enter symbol: ")
    print("The symbol is:", text)

    while True:
        answer = input("Do you want to continue? (yes/no): ")

        if answer == "yes":
            print("You agreed. The symbol is:", text)
            return
        elif answer == "no":
            print("You can change the text.")
            text = input("Enter new text: ")
            print("The new text is:", text)
        else:
            print("Invalid answer. Please type 'yes' or 'no'.")


calculatorsymb()
