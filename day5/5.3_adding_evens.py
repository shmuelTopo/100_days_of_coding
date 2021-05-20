total_even = 0
for num in range(1, 101):
    if num % 2 == 0:
        total_even += num
print(f'The total even numbers between 1 and 100 is {total_even}')

total = 0
for num in range(2, 101, 2):
    total += num
print(total)