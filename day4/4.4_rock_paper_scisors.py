import random


def print_hand(num):
    if num == 0:
        print(rock)
    elif num == 1:
        print(paper)
    elif num == 2:
        print(scissors)
    else:
        print('Unknown value')


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def game():
    try:
        user_hand = int(
            input('What do you choose? type 0 for rock, 1 for paper, or 2 for scissors.\n'))
    except ValueError:
        print('You didn\'t enter a real number, choose again')
        return False

    if user_hand < 0 or user_hand > 2:
        print('You didn\'t enter a number between 0-2, try again')
        return False

    print_hand(user_hand)

    comp_hand = random.randint(0, 2)
    print('Computer choose:')
    print_hand(comp_hand)

    if comp_hand == user_hand:
        print('a tie')
        return True

    if (comp_hand == 0 and user_hand == 2) or (comp_hand == 1 and user_hand == 0) or (comp_hand == 2 and user_hand == 1):
        print('Computer won the game')
    else:
        print('You won the game')
    return True


while True:
    good_input = game()
    if good_input:
        answer = input('Wanna play again? answer "y" or "n" ')
        if answer[0].lower() != 'y':
            break
