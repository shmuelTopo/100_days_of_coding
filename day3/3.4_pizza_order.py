# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 0
if size.lower() == 's':
    price += 15
elif size.lower() == 'm':
    price += 20
elif size.lower() == 'l':
    price += 25

if add_pepperoni.lower() == 'y':
        price += 2
        if(size.lower() != 's'):
            price += 1
if extra_cheese == 'y':
        price += 1

print(f'You total bill is ${price}')

