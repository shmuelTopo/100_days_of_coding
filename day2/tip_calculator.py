print('Welcome to the tip calculator')
bill_cost = int(input('What was the total bill? '))
num_of_people = int(input('How many people split the bill? '))
tip = int(input('What percentage tip would you like to give? 10 12 or 15? '))
pay = bill_cost + ((bill_cost / 100) * tip)
print(f'Each person should pay {pay / num_of_people}')


