import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
num_of_people = len(names)
random_person = random.randint(0, num_of_people - 1)

print(f'{names[random_person].capitalize()} is going to buy the meal today!')
