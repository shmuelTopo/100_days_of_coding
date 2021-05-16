# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_to_live = 90 - int(age)
days_left = years_to_live * 365
weeks_left = years_to_live * 52
month_left = years_to_live * 12
print(f'You have {int(days_left)} days, {int(weeks_left)} weeks, and {int(month_left)} month left')