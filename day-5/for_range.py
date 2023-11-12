total_even_numbers = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even_numbers += i
print(total_even_numbers)

total = 0
for number in range(2, 101, 2):
    total += number
print(total)