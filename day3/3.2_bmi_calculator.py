# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height **2 

if bmi >= 35:
    condition = 'clinically obese'
elif bmi >= 30:
    condition = 'obese'
elif bmi >= 25:
    condition = 'slightly overweight'
elif bmi >= 20:
    condition = 'normal weight'
elif bmi >= 18.5:
    condition = 'underweight'

print(f'Your BMI is {int(bmi + 0.5)}, you are {condition}.')




