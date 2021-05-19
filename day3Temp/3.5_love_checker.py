# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

score_true = 0
score_love = 0
for letter in (name1 + name2):
    if letter.lower() in 'true':
        score_true += 1

for letter in (name1 + name2):
    if letter.lower() in 'love':
        score_love += 1

score = score_true * 10 + score_love

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
