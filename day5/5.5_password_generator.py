# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(
    input("How many letters would you like in your password?\n"))
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for char in range(num_of_letters):
    password += random.choice(letters)
for char in range(num_of_symbols):
    password += random.choice(symbols)
for char in range(num_of_numbers):
    password += random.choice(numbers)

print(f'Your easy passwor is {password}')

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = list(password)
random.shuffle(password)
password = ''.join(password)

print(f'You mix password is {password}')


password_len = num_of_letters + num_of_symbols + num_of_numbers
password = ''
type_of_charecter = ['letter', 'symbol', 'number']
letters_used = 0
symbols_used = 0
numbers_used = 0
for _ in range(password_len):
    type = random.choice(type_of_charecter)
    if(type == 'letter'):
        password = password + random.choice(letters)
        letters_used += 1

    elif(type == 'symbol'):
        password = password + random.choice(symbols)
        symbols_used += 1

    else:
        password = password + random.choice(numbers)
        numbers_used += 1

    if 'letter' in type_of_charecter and letters_used == num_of_letters:
        type_of_charecter.remove('letter')

    if 'symbol' in type_of_charecter and symbols_used == num_of_symbols:
        type_of_charecter.remove('symbol')

    if 'number' in type_of_charecter and numbers_used == num_of_numbers:
        type_of_charecter.remove('number')

print(f'The password I generated is {password}')
