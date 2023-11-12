# Leap year challenge
year = int(input("Enter a year: "))
# Checking leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")