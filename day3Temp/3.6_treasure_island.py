print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


def play_game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    out_of_forest = input('''You coming out of a forest, you see a lion you right in front of you
    will you run back into the forest or jump on a tree? type your answer "run" or "tree"
    ''')

    if out_of_forest.lower() != 'tree':
        print('You fall on the ground the lion eat the "kishkes" out of you, game over')
        return False

    back_into_forest = input('''You wait on the tree for couple of minutes until the lion goes away
    then when you go down you hear human voice calling for help deep inside the forest
    you go inside the forest to help the voice, or leave the forest and stay out of trouble? type "inside" or "leave"
    ''')

    if back_into_forest.lower() != 'inside':
        print('''You go toward the end of the forest when you feel reliefe that you escapes the lion, 
        he comes out again and kill you in seconds, you are dead, game over''')
        return False

    river = input('''You going towards the voice and you find out that it's across the river
    swim the river or build a boat? answer "swim" or "boat"
    ''')

    if river.lower() != 'boat':
        print('''You swim the river when a big green crocodlie eat you alive
        Game over!! ''')
        return False

    is_pray = input('''You find and axe on the ground and build the boat
    after few minutes you stop hearing the voice of "help" 
    you not sure what to do, do you pray for god or leave the forest? answer "pray" or "leave"
    ''')

    if is_pray.lower() != 'pray':
        print('''You start walking towards the exit of the forest and fall in a hole and die
        grame over!
        ''')
        return False

    cross_road = input('''You start praying, when you hear a voice behind your back of 
    a person holding a key and telling you that there is a treasure behind the river
    and he hand you over a map and a key, you finishing building the boat and cross the river
    you come to the edge and check the map and follow the map 
    there is a hole in the map and you not sure if to make a left turn or a right turn
    you make a left turn or right? answer "right" or "left"
    ''')

    if cross_road != 'right':
        print('''You make a left and continue for 10 minutes when you relize that you should of make right
        a witch comes out of nowhere and kill you with a course
        Game over
        ''')
        return False

    tree = input('''You make a right and you continue to follow the map when you come the end of the directions
    you see 3 trees the treasure most bee in one of them, but which one
    every tree has a different color, red black and green 
    and the map say that the treasor is in the 绿色 tree You don't know chineese but you make a guess
    which color do you choose? answer "black", "green" or "red"
    ''')

    if tree.lower() != 'green':
        print('''You die
        game over!
        ''')
        return False
    else:
        print('You found the treasure You won the game!!!')


play_game()
