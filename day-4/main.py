import random
random_choice = random.randint(0, 1)
user_choice = int(input("Enter a number between 0-1: "))
if user_choice == random_choice:
    if user_choice == 0:
        print("Heads")
    else:
        print("Tails")
else:
    print("Kindly enter a number between 0-1")