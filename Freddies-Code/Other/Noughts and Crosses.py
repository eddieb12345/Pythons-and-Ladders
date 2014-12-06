#gameover = False
#current_player = ''
#board = []

#def board_setup():                                                              #Sets the settings to default
gameover = False
current_player = 'Player 1'
board = []
for n in range(3):                                                          #Setting up the board
    board.append(['\u25a1']*3)

def print_board():                                                              #Prints the board neatly
    for row in board:
        print(" ".join(row))

print('Welcome to noughts and crosses!')

#board_setup()


while gameover == False:                                                        #Checks the game is still going
                                                                                #Checks for possible winning combinations
       #or board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'\
       #or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'\
       #or board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'\
       #or board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'\
       #or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'\
       #or board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'\
       #or board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':     


    p1win = True
    
    for col in range(len(board)):
        if board[0][col] != 'X':
            p1win = False
            

    if p1win == True:        
        print_board()
        print('Payer 1 wins!')
        gameover = True
        break
    
    if board[0][0] == 'O' and board[0][1] == 'O' and board [0][2] == 'O'\
       or board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'\
       or board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'\
       or board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'\
       or board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'\
       or board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'\
       or board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'\
       or board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':     
        print_board()
        print('Payer 2 wins!')
        gameover = True
        break

    draw = True
    
    for n in range(len(board)):                     
        if '\u25a1' in board[n]:
            draw = False

    if draw == True:
        print_board()
        print('It\'s a draw.')
        gameover = True
        break

    print_board()
    print(current_player + ' it\'s your go.')

    raw_col = eval(input('Enter the column of the square you want: '))          #Player chooses a square
    raw_row = eval(input('Enter the row of the square you want: '))
    col = raw_col - 1                                                           #Converts normal numbers to list positions                          
    row = raw_row - 1

    if col > 2 or row > 2:                                                      #Checks that the square is inside the board
        print('Thats outside the board, please try again!')

    elif board[row][col] == 'X' or board[row][col] == 'O':                      #Checks that the square is blank
        print('That square is already taken, please try again!')

    else:                                           
        if current_player == 'Player 1':                                        #Makes the move and changes the player
            board[row][col] = 'X'                                               
            current_player = 'Player 2'
        elif current_player == 'Player 2':
            board[row][col] = 'O'
            current_player = 'Player 1'       



