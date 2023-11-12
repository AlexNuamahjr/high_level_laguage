print("Welcome to the rollercoaster!")
height = int(input("What is your height in centimeter: "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child cost is $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket cost is $7.")
    elif age >= 45 and age <= 55:
        print("Your ride is free")
    else:
        bill = 12
        print("Adult ticket cost is $12.")
    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "y":
        bill += 3
    print(f"your final bill is ${bill}")
    

else:
    print("you can't ride")