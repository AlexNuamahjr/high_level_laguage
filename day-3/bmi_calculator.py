height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in kilogram: "))
bmi = round(weight / height ** 2)

# checking bmi
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you're under weight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and your weight is normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you're overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you're obese.")
else:
    print(f"Your BMI is {bmi} and you're clinically obese.")