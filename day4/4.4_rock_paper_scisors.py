import random

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

game_images = [rock, paper, scissors]


def game():
    try:
        user_choice = int(
            input('What do you choose? type 0 for rock, 1 for paper, or 2 for scissors.\n'))
    except ValueError:
        print('You didn\'t enter a real number, you lose')
        return

    if user_choice < 0 or user_choice > 2:
        print('You typed invalid number, You lose!')
        return

    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print('Computer choose:')
    print(game_images[computer_choice])

    if computer_choice == user_choice:
        print('it\'s a draw')
        return

    if (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
        print('You lose')
    else:
        print('You won!')
    return True


while True:
    game()
    answer = input('Wanna play again? answer "y" or "n" ')
    if answer.lower() != 'y' and answer.lower() != 'yes':
        break
