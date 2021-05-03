import random


#TicTacToe game
#define the printing function
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('------')
    print(board[6] + '|' + board[7] + '|' + board[8])

    
# Greetings and user character delegation
def welcome_game():
    print('Welcome to Tic Tac Toe!')

    # Valid choices to pick
    player_choice = ['X', 'O']
    choice = 'wrong'
    comp = 'empty'
    while choice not in player_choice:
        
        choice = input('Do you want to be X or O? ').upper()

        #Check if the user choice exists in the list of choices
        if choice not in player_choice:
            print('Sorry that is not a valid choice!')
        else:
            print('Player picked: ' + choice)
            if choice == player_choice[0]:
                print('Computer will be: ' + player_choice[1])
                comp = player_choice[1]
            else:
                print ('Computer will be : ' + player_choice[0])
                comp = player_choice[0]
  
    return choice,comp
                

def game_status(theboard):

    # end game checker flag
    end_game = 'n'

    
    # check if any of the cells equate to each other 
    if (theboard[0] == theboard[1] == theboard[2]):
        end_game = 'y'
    elif (theboard[3] == theboard[4] == theboard[5]):
        end_game = 'y'
    elif (theboard[6] == theboard[7] == theboard[8]):
        end_game = 'y'
    elif (theboard[0] == theboard[3] == theboard[6]):
        end_game = 'y'
    elif (theboard[1] == theboard[4] == theboard[7]):
        end_game = 'y'
    elif (theboard[2] == theboard[5] == theboard[8]):
        end_game = 'y'
    elif (theboard[0] == theboard[4] == theboard[8]):
        end_game = 'y'
    elif (theboard[2] == theboard[4] == theboard[6]):
        end_game = 'y'
    else:
        pass

    # End game if someone won
    if end_game == 'y':
        print('Game Over!')
        return 'end'

    

# Iterate through to update the values of theboard
def populate(user, comp):
    
    theboard = ['0','1','2',
            '3','4','5',
            '6','7','8']
    printBoard(theboard)
    game = 'go'
    while game != 'end':


        finish = 'n'
        location = int(input('Enter the location: '))
        
        while finish != 'y':
            if theboard[location] != 'X' and theboard[location] != 'O':
                theboard[location] = user
                #printBoard(theboard)
                finish = 'y'
            else:
                location = int(input('Sorry that location is taken. Try again: '))

        finish = 'n'
        computer = random.randint(0, 8)
        
        while finish != 'y':
            if theboard[computer] != 'X' and theboard[computer] != 'O':
                theboard[computer] = comp
                finish = 'y'
                printBoard(theboard)
            else:
                computer = random.randint(0,8)

        game = game_status(theboard)


# Main game functions callout
if __name__ == '__main__':
    play = 'y'
    while (play == 'y'):

        #start the game
        user,comp = welcome_game()
        populate(user, comp)

        #Ask user if the still want to play
        play = input('Would you like to play again?: ')

        #If answer is no, end the game
        if play == 'n':
            print('Thank you for playing this game')
            print('Goodbye')
   
