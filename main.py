
# BMI Calculator
if __name__ == "__main__":

    name1 = input("Please enter your first name: ")
    height_inches1 = int(input("Please enter your height in inches (12 inches = 1 foot): "))
    weight_lbs1 = int(input("Please enter your weight in pounds: "))

    def bmi_calculator(name, height_inches, weight_lbs):

        def bmi_calc():
            bmi_math = weight_lbs / (height_inches ** 2)
            return bmi_math

        bmi = bmi_calc()

        if bmi < 25:
            return f"{name} is not overweight because their BMI is less than 25 at {bmi:.2f}."
        else:
            return f"{name} is overweight because their BMI is greater than 25 at {bmi:.2f}."


    result1 = bmi_calculator(name1, height_inches1, weight_lbs1)

    print(result1)
