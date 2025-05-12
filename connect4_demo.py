# constant variable declarations
HEIGHT = 6
WIDTH = 7

# Function declarations
def initialize():
    ''' Sets up the empty board. '''
    board = []
    
    # For all 6 rows
    for i in range(HEIGHT):
        board.append(["O"] * WIDTH) # add a list of 7 columns to the current row

    # end the function
    return board

def print_board(board):
    ''' Prints out a correct formatted board. '''

    # prints out column numbers above each column for easier user input
    print ("1 2 3 4 5 6 7") 
    
    # separates column numbers from the board
    print("_" * 13) 
    
    # the program doesn't actually know what each "row" is
    # instead, it looks at the list, and looks for where each value ends
    # our list looks like this: [[7 columns], [7 columns], [7 columns], [7 columns], [7 columns], [7 columns]]
    # since each list of 7 columns (a row) is separated by a comma, the code will take ALL of the columns before each comma 
    # and say that is one "row"
    # but we can change "row" here to literally ANYTHING, even "skibidi_fortnite", and as long as we change it in both places,
    # it will still work
    for row in board:
        print("|".join(row)) # this code looks at the row (which was grabbed from above), then replaces all the commas with "|"

def get_move(board, player):
    ''' 
        Takes the board and the player as parameter. 
        Asks the player to input a column and checks if the entry is valid. 
    '''
    move = int(input("Player {} please enter the column you want to drop your piece into: ".format(player)))

    # check if the move is on the board
    if (move < 1 or move > WIDTH):
        print("You cannot move there. Your move can be a number between 1 and 7.")
        move = get_move(board, player)

    # python lists start at 0, but we show the player a list starting at 1 when they make their move
    # so, we have to adjust the user input so it matches up with what python is expecting
    move = move - 1

    # check if the column is full
    column_full = True
    for row in range(HEIGHT):
        if board[row][move] == "O": # if the current place on the board is empty,
            column_full = False # tell the computer the column isn't full.
            break # ends loop as soon as we see the column isn't full
       
    if column_full:
        print("The column you chose is full. Please choose a different column.")
        move = get_move(board, player)
    
    # with all of our checks out of the way, we can now tell the rest of the program
    # where the player moved
    return move

def make_move(board, player, column):
    ''' 
        Takes the board, the player, and the player's entry. 
        Makes the move based on the board configuration and the entry. 
    '''
    # this stores where the piece will go
    move = 0
    
    # we are going to go through every row for the column given
    # at every empty space, we update where the piece will go
    # once we run out of empty spaces, the loop ends
    # this way, we always choose the lowest empty space! 
    for row in range(HEIGHT):
        if board[row][column] == "O":
            move = row
        else: # activates only after we have seen the last empty space
            break
    
    # changes the board at the selected place to
    # the letter that represents that player's pieces
    board[move][column] = player
    
    # give the board back to the rest of the code
    return board


def check_win(board):
    ''' 
        This function takes the board as a parameter and checks if someone has won the game. 
        If so, it returns the player that has won. 
        Otherwise, it returns an empty string. 
    '''
    # Check horizontal for winner
    for row in range(HEIGHT):
        for col in range(WIDTH - 3):
            if (board[row][col] == board[row][col + 1] == \
            board[row][col + 2] == board[row][col + 3]) \
            and (board[row][col] != "O"):
                return board[row][col]
    
    # Check vertical for winner
    for col in range(WIDTH):
        for row in range(HEIGHT - 3):
            if (board[row][col] == board[row + 1][col] == \
            board[row + 2][col] == board[row + 3][col]) and \
            (board[row][col] != "O"):
                return board[row][col]

    # Check diagonal (top-left to bottom-right) for winner
    for row in range(HEIGHT - 3):
        for col in range(WIDTH - 3):
            if (board[row][col] == board[row + 1][col + 1] == \
            board[row + 2][col + 2] == board[row + 3][col + 3]) \
            and (board[row][col] != "O"):
                return board[row][col]
    
    # Check diagonal (bottom-left to top-right) for winner
    for row in range(HEIGHT - 1, HEIGHT - 3, -1):
        for col in range(WIDTH - 3):
            if (board[row][col] == board[row - 1][col + 1] == \
            board[row - 2][col + 2] == board[row - 3][col + 3]) \
            and (board[row][col] != "O"):
                return board[row][col]
    
    # Check if board is full
    full = True
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if board[row][col] == "O":
                full = False
                break
    if full:
        return "Tie"
    
    # If none of the above are true then the game is not over
    return ""


# Main game logic
def main():
    ''' Sets up the game and runs the game loop until the game is over. '''

    board = initialize()
    player = "R"
    winner = ""
    
    while winner == "":
        print_board(board)
        col = get_move(board, player)
        make_move(board, player, col)
        winner = check_win(board)
        if player == "R":
            player = "B"
        else:
            player = "R"
    print_board(board)
    if winner == "Tie":
        print("Tie game.")
    else:
        print("Player {} wins!".format(winner))

if __name__ == "__main__":
    main()