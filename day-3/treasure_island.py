print("*** Welcome to Treasure Island ***\n"
    " *** Your mission is to find the treasure ***")
user_choice = input("Do you want to go left or right?: ").lower()

if user_choice == "left":
    user_choice = input("Do you want to wait or swim?: ").lower()
    if user_choice == "wait":
        user_choice = input("which door, 'red', 'blue' or 'yellow'?: ").lower()
        if user_choice == "yellow":
            print("You win!!")
        else:
            print("Game Over!!")
    else:
        print("Game Over!!!")
else:
    print("Game Over")
