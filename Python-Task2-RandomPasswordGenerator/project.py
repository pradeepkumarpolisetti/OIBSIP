import random
import string

print("Welcome to the Random Password Generator!")

while True:
    try:
        a = int(input("Enter password length (minimum 8): "))

        if a < 8:
            print("Password length must be at least 8.")
            continue

        print("Choose at least 2 character types.")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        b = input("Enter your choices (example: 123): ")

        c = ""

        if "1" in b:
            c += string.ascii_uppercase
        if "2" in b:
            c += string.ascii_lowercase
        if "3" in b:
            c += string.digits
        if "4" in b:
            c += string.punctuation

        if len(c) == 0:
            print("Please select character types.")
            continue

        if len(set(b)) < 2:
            print("Please select at least 2 character types.")
            continue

        d = ""

        for i in range(a):
            d += random.choice(c)

        print("Generated Password:", d)

        e = input("Generate another password? (y/n): ")

        if e.lower() != "y":
            print("Thank you!")
            break

    except ValueError:
        print("Please enter a valid number!")
