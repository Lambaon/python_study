def main():
    print("You have to enter a choice F-Fahrenheit, K-Kelvin")

    while True:
        choice = input("Enter your choice: ")
        celsius = float(input("Enter temperature in Celsius: "))
        if choice == "F" or choice == "Fahrenheit" or choice == "f":
            fahrenheit = (celsius * 9 / 5) + 32
            print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
        elif choice == "K" or choice == "Kelvin" or choice == "k":
            kelvin = celsius + 273.15
            print("Temperature in Kelvin: {:.2f}".format(kelvin))
        elif choice == " ":
            print("invalid ty")
        else:
            print("Invalid answer. Please type like in choice.")
        exit()


main()
