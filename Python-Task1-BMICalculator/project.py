print("Welcome to the BMI Calculator!")

while True:
    try:
        a = float(input("Enter your weight in kg: "))
        b = float(input("Enter your height in metres: "))

        if a <= 0 or b <= 0:
            print("Weight and height must be positive!")
            continue

        c = a / (b * b)

        print("Your BMI is:", round(c, 2))

        if c < 18.5:
            print("Category: Underweight")
        elif c < 25:
            print("Category: Normal")
        elif c < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

        break

    except ValueError:
        print("Please enter numbers only!")
