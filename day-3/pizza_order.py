print("welcome to pizza deliveries")
size = input("What size pizza do you want? S, M, L: ").lower()
add_pepperoni = input("Do you want to add pepperoni? Y or N: ").lower()
add_extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small = 2
pepperoni_for_medium_large = 3
extra_cheese = 1
bill = 0

if size == "s":
    bill = small_pizza
    if add_pepperoni == "y":
        bill += pepperoni_for_small
    if add_extra_cheese == "y":
        bill += extra_cheese
    print(f"Your final bill is ${bill}")
elif size == "m":
    bill = medium_pizza
    if add_pepperoni == "y":
        bill += pepperoni_for_medium_large
    if add_extra_cheese == "y":
            bill += extra_cheese
    print(f"Your final bill is ${bill}")
else:
    bill = large_pizza
    if add_pepperoni == "y":
        bill += pepperoni_for_medium_large
    if add_extra_cheese == "y":
        bill += extra_cheese
    print(f"Your final bill is ${bill}")
