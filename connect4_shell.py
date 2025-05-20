# constant variable declarations
HEIGHT = 6 # height of board - number of rows
WIDTH = 7 # width of board - number of columns

# function declarations
def initialize():
    '''Sets up the empty board.'''
    # make a new list called board
    board = []
    for row in range(HEIGHT): # loop for how many rows there are
        board.append(["O"] * WIDTH)   # on each row, add a column to the list.
                                            # in python, multiplying in a list adds that number of items to it
                                            # so "O" * 8 would add 8 O's to the list
    return board

def print_board(board):
    '''Prints out the board correctly.'''
    print("1 2 3 4 5 6 7") # print the column numbers (so the players know what they can input)
    print("_" * 13) # print out a separator "_" to separate the column numbers from the board
    for row in board: 
        print(row) # print out each row on a separate line
                    # print(board) would print out all rows on the same line

def get_move(board, player):
    '''Takes in the user's move and verifies it.'''

    # player picks a column
    move = int(input("Please put in a number 1-7 for where you want to drop your piece."))
    
    # make sure move is between columns 1-7
    if (move < 1 or move > WIDTH):
        get_move(board, player)

    # check if column is full
    # column_full = True
    for row in range(HEIGHT):
        if board[move][row] == "O":
            column_full = False
    
    if(column_full):
        get_move(board,player)
    else:
        return move

def make_move(move, board, player):
    '''Changes the board using the user's move.'''
    # steps we need to take to finish the code
    
    # using the move,
    # look at the board at that column
    # then, replace the lowest "O" 
    # with the letter of the player whose turn it is
    
    # board -> column -> at the last empty space
    # board[column][last empty space] = player
    
    # FOR LOOP
        # we're going down through the row
        # on each row, look at the current cell of the list
        # if it is equal to "O", keep going
            # a variable to track where the move goes
        # if it isn't, stop going

    # update the board

    return



def check_win(board):
    '''Checks the whole board to see if a player has connected 4!'''
    
    # We check all four directions separately:
    # Side-to-side
    for row in range(HEIGHT):
        for col in range(WIDTH - 3):
            if (board[row][col] == board[row][col + 1] == \
                board[row][col + 2] == board[row][col + 3]) \
                and (board[row][col] != "O"):
                    return board[row][col]
    
    # Up-to-down
        # loop through board's columns instead of its rows
        # then, loop through each row for that column
        # check to see - like above - if any four rows have the same value and aren't "O"
            # then return board[row][col] if true

    # Diagonal: Top-left to bottom-right

    # Diagonal: Bottom-left to top-right
        # we will need to use the "step" parameter for 
        # python's range function: https://www.w3schools.com/python/ref_func_range.asp

    return ""

# main game loop 
def main():
    '''Runs the actual game.'''
    board = initialize()
    player = "R" # red goes first
    winner = ""

    while winner == "":
        print_board()
            # get the current player's move
            # make the current player's move
            # check to see if anyone has won
            # change the current player
        break
    
    # this code will run only after "winner" has a value
    # because the loop runs while "winner" is empty
    print_board(board)
    if winner == "Tie":
        print("Tie game.")
    else: 
        print("Player {} wins!".format(winner))

# program bootstrap
if __name__ == "__main__":
    main()