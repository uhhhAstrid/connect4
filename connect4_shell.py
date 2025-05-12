# constant variable declarations
HEIGHT = ??? # height of board
WIDTH = ??? # width of board

# function declarations
def initialize():
    '''Sets up the empty board.'''
    return

def print_board(???):
    '''Prints out the board correctly.'''
    return

def get_move(???, ???):
    '''Takes in the user's move and verifies it.'''
    return

def make_move(???, ???, ???):
    '''Changes the board using the user's move.'''
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
        # game goes here!
        # we need to:
            # print the board
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