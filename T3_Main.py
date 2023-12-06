# initialize global variables
play_again = True


def check_winner(gamestate):
    # check horizontals
    if gamestate[0][0] != '_' and gamestate[0][0] == gamestate[0][1] and gamestate[0][0] == gamestate[0][2]:
        return gamestate[0][0]
    elif gamestate[1][0] != '_' and gamestate[1][0] == gamestate[1][1] and gamestate[1][0] == gamestate[1][2]:
        return gamestate[1][0]
    elif gamestate[2][0] != '_' and gamestate[2][0] == gamestate[2][1] and gamestate[2][0] == gamestate[2][2]:
        return gamestate[2][0]
    # check verticals
    elif gamestate[0][0] != '_' and gamestate[0][0] == gamestate[1][0] and gamestate[0][0] == gamestate[2][0]:
        return gamestate[0][0]
    elif gamestate[0][1] != '_' and gamestate[0][1] == gamestate[1][1] and gamestate[0][1] == gamestate[2][1]:
        return gamestate[0][1]
    elif gamestate[0][2] != '_' and gamestate[0][2] == gamestate[1][2] and gamestate[0][2] == gamestate[2][2]:
        return gamestate[0][2]
    # check diagonals or return no winner
    elif gamestate[0][0] != '_' and gamestate[0][0] == gamestate[1][1] and gamestate[0][0] == gamestate[2][2]:
        return gamestate[0][0]
    elif gamestate[2][0] != '_' and gamestate[2][0] == gamestate[1][1] and gamestate[2][0] == gamestate[0][2]:
        return gamestate[2][0]
    else:
        return 'none'


# displaying the current state of the game board
def print_gamestate():
    print('  1 2 3')
    print(f'A {gamestate[0][0]}|{gamestate[0][1]}|{gamestate[0][2]}')
    print(f'B {gamestate[1][0]}|{gamestate[1][1]}|{gamestate[1][2]}')
    print(f'C {gamestate[2][0]}|{gamestate[2][1]}|{gamestate[2][2]}')


# instructions for message for player moves
def cord_error():
    print('Please enter your moves in the form of [Letter][Number]')


# logic for updating the game state and forcing players to move on empty spaces
def turn(player):
    while True:
        cordin = input(f'It is {player}\'s turn: ')
        while len(cordin) != 2:
            cord_error()
            cordin = input(f'It is {player}\'s turn: ')
        cordin = list(cordin)
        if int(cordin[1]) < 1 or int(cordin[1]) > 3:
            cord_error()
        elif cordin[0] == 'a' or cordin[0] == 'A':
            cordin[0] = '0'
            if gamestate[int(cordin[0])][int(cordin[1]) - 1] == '_':
                gamestate[int(cordin[0])][int(cordin[1]) - 1] = player
                break
            else:
                print('Please select an empty space')
        elif cordin[0] == 'b' or cordin[0] == 'B':
            cordin[0] = '1'
            if gamestate[int(cordin[0])][int(cordin[1]) - 1] == '_':
                gamestate[int(cordin[0])][int(cordin[1]) - 1] = player
                break
            else:
                print('Please select an empty space')
        elif cordin[0] == 'c' or cordin[0] == 'C':
            cordin[0] = '2'
            if gamestate[int(cordin[0])][int(cordin[1]) - 1] == '_':
                gamestate[int(cordin[0])][int(cordin[1]) - 1] = player
                break
            else:
                print('Please select an empty space')
        else:
            cord_error()


def ask_play_again():
    answer = input('Play again? (Yes/No): ')
    while True:
        if answer == 'N' or answer == 'n' or answer == 'No' or answer == 'no':
            return False
        elif answer == 'Y' or answer == 'y' or answer == 'Yes' or answer == 'yes':
            return True
        else:
            answer = input('Please use a valid answer (Yes/No): ')


# main loop
while play_again:
    # initialize variables
    gamestate = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    # gamestate visual reference:
    #       1      2      3
    #  A  [0][0] [0][1] [0][2]
    #  B  [1][0] [1][1] [1][2]
    #  C  [2][0] [2][1] [2][2]
    winner = 'none'
    turn_counter = 0

    # first player character selection
    player1 = input('Player 1, choose your character: ')
    while len(player1) > 1:
        player1 = input('Player 1, please choose only a single character: ')

    # second player character selection, must be different from p1
    player2 = input('Player 2, choose your character: ')
    while player2 == player1 or len(player2) > 1:
        if player2 == player1:
            player2 = input('Player 2, please choose a different character: ')
        if len(player2) > 1:
            player2 = input('Player 2, please choose only a single character: ')

    # display initial game board and instructions to play
    print_gamestate()
    cord_error()

    # gameplay loop
    while winner == 'none':
        turn(player1)
        print_gamestate()
        winner = check_winner(gamestate)
        turn_counter += 1
        if winner != 'none' or turn_counter == 9:
            break
        turn(player2)
        print_gamestate()
        winner = check_winner(gamestate)
        turn_counter += 1

    # end of game message and play again check
    if turn_counter == 9:
        print('------------------')
        print(f'|      Draw      |')
        print('------------------')
    else:
        print('-------------------')
        print(f'|     {winner} Wins!     |')
        print('-------------------')

    play_again = ask_play_again()

print('Goodbye!')
