# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

from random import randint as ran
head_or_talis = ran(0, 1)
if head_or_talis:
    print('Heads')
else:
    print('Tails')
