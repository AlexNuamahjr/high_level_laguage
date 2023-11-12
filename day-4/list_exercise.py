import random
names = input("Give me everybody's names, seperated by a  comma:\n")
every_body = names.split(", ")
# num_of_items = len(every_body)

# choice = random.randint(0, num_of_items -1)
# financer = every_body[choice]
financer = random.choice(every_body)
print(f"{financer} is paying for the bill")