# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


# Write your code below this row 👇
highest = 0
for score in student_heights:
    if score > highest:
        highest = score
print(f'The highest score is {highest}')
