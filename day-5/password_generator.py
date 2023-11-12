# password generator
import random
alphabeths = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j"
             "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", 
             "v", "w", "x", "y", "z", "A", "B", "C", "D", "E",
             "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
             "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "*", "(", ")", "+", "_"]
print("***Welcome to my python password generator!***")
amount_of_letters = int(input("How many letter would you like in your password?: "))
amount_of_nums = int(input("How many numbers will you like in your password?: "))
amount_of_symbols = int(input("How many symbols will you like in your password?: "))

password = []
for character in range(1, amount_of_letters, + 1):
   password.append(random.choice(alphabeths))

for number in range(1, amount_of_nums, + 1):
   password.append(random.choice(numbers))

for symbol in range(1, amount_of_symbols, + 1):
   password.append(random.choice(symbols))

random.shuffle(password)

final_password = "".join(password)
print(f"Your password is: {final_password}")
