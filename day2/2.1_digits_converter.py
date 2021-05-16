# 🚨 Don't change the code below 👇
two_digit_number = int(input("Type a two digit number: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

num1 = two_digit_number // 10
num2 = two_digit_number - (num1 * 10)

print(f'{num1} + {num2} = {num1 + num2}')