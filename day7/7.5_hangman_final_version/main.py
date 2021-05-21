import random
from word_list import word_list
from arts import stages
from arts import logo
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = list('_' * len(chosen_word))
letter_used = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in letter_used:
        print('You already picked this letter, try a different one...')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            letter_used.append(letter)

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f'The letter {guess} is not in the word, you lose a life. ')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. the word i picked was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])

exit = input('To exit the game click Enter...')
