print("Welcome to Love Calculator")
name1 = input("Enter your name:\n").lower()
name2 = input("Enter your name:\n").lower()

combined_string = name1 + name2
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t + r + u + e
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, and you go together like coke and mentor")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, and you are alright together")
else:
    print(f"Your score is {love_score}")
    