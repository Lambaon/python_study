import random


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 7

    print("Введіть перше число: ")
    print(f"У тебе є {attempts} спрб ")

    while attempts > 0:
        try:
            guess = int(input("Введи своє число"))
        except ValueError:
            print("She raz!")
            continue

        if guess == secret_number:
            print("You guessed correctly")
            return
        elif guess < secret_number:
            print("Too low")
        else:
            print("Too high")

        attempts -= 1
        print(f"Zalishilos stilki sprob {attempts}")

    print(f"proigral dura {secret_number}")


guess_number()
