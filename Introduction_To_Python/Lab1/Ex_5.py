from random import randint
# --------- Global Variables -----------


board = [" ", " ", " ",  # Will hold our game board data
         " ", " ", " ",
         " ", " ", " "]

game_still_going = True  # Lets us know if the game is over yet

winner = None  # Tells us who the winner is

current_player = "X"  # Tells us who the current player is (X goes first)

computer = None  # Tells if we are playing vs computer

# ------------- Functions ---------------


def play_game():  # Play a game of tic tac toe
    display_board()   # Show the initial game board
    choose_opponent()  # Choose opponent (computer or human)
    while game_still_going:  # Loop until the game stops (winner or tie)

        handle_turn(current_player)  # Handle a turn

        check_if_game_over()  # Check if the game is over

        flip_player()  # Flip to the other player

    if winner == "X" or winner == "O":  # Since the game is over, print the winner or tie
        print(winner, " won.")
    elif not winner:  # == None:
        print("Tie.")


def display_board():  # Display the game board to the screen
    print("\n")
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |" + "     1 | 2 | 3")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |" + "     4 | 5 | 6")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |" + "     7 | 8 | 9")
    print("-------------")
    print("\n")


def handle_turn(player):  # Handle a turn for an arbitrary player
    global computer
    if not computer:
        print(player + "'s turn.")   # Get position from player
        position = input("Choose a position from 1-9: ")

        valid = False  # Whatever the user inputs, make sure it is a valid input, and the spot is open
        while not valid:

            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # Make sure the input is valid
                position = input("Choose a position from 1-9: ")

            position = int(position) - 1  # Get correct index in our board list

            if board[position] == " ":   # Then also make sure the spot is available on the board
                valid = True
            else:
                print("You can't go there. Go again.")
    else:
        if player == "X":
            print(player + "'s turn.")  # Get position from player
            position = input("Choose a position from 1-9: ")

            valid = False  # Whatever the user inputs, make sure it is a valid input, and the spot is open
            while not valid:

                while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # Make sure the input is valid
                    position = input("Choose a position from 1-9: ")

                position = int(position) - 1  # Get correct index in our board list

                if board[position] == " ":  # Then also make sure the spot is available on the board
                    valid = True
                else:
                    print("You can't go there. Go again.")
        else:  # Get move from computer
            position = randint(0, 8)

            valid = False
            while not valid:
                if board[position] == " ":
                    valid = True
                else:
                    position = randint(0, 8)

    board[position] = player  # Put the game piece on the board

    display_board()  # Show the game board


def check_if_game_over():  # Check if the game is over
    check_for_winner()
    check_for_tie()


def check_for_winner():  # Check to see if somebody has won
    global winner  # Set global variables
    row_winner = check_rows()  # Check if there was a winner anywhere
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:  # Get the winner
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():  # Check the rows for a win
    global game_still_going  # Set global variables
    row_1 = board[0] == board[1] == board[2] != " "  # Check if any of rows have all the same value (and is not empty)
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    if row_1 or row_2 or row_3:  # If any row does have a match, flag that there is a win
        game_still_going = False
    if row_1:  # Return the winner
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:  # Or return None if there was no winner
        return None


def check_columns():  # Check the columns for a win
    global game_still_going  # Set global variables
    column_1 = board[0] == board[3] == board[6] != " "  # Check if any of the columns have all the same value
    column_2 = board[1] == board[4] == board[7] != " "
    column_3 = board[2] == board[5] == board[8] != " "
    if column_1 or column_2 or column_3:  # If any row does have a match, flag that there is a win
        game_still_going = False
    if column_1:  # Return the winner
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:  # Or return None if there was no winner
        return None


def check_diagonals():  # Check the diagonals for a win
    global game_still_going  # Set global variables
    diagonal_1 = board[0] == board[4] == board[8] != " "  # Check if any of the columns have all the same value
    diagonal_2 = board[2] == board[4] == board[6] != " "
    if diagonal_1 or diagonal_2:  # If any row does have a match, flag that there is a win
        game_still_going = False
    if diagonal_1:  # Return the winner
        return board[0]
    elif diagonal_2:
        return board[2]
    else:  # Or return None if there was no winner
        return None


def check_for_tie():  # Check if there is a tie
    global game_still_going  # Set global variables
    if " " not in board:  # If board is full
        game_still_going = False
        return True
    else:  # Else there is no tie
        return False


def flip_player():  # Flip the current player from X to O, or O to X
    global current_player  # Global variables we need
    if current_player == "X":  # If the current player was X, make it O
        current_player = "O"
    elif current_player == "O":  # Or if the current player was O, make it X
        current_player = "X"


def choose_opponent():
    global computer  # Set global variables
    ans = input("Would You like to play vs computer? (y - yes/n - no)")
    if ans == "y" or ans == "Y":
        computer = True
    else:
        computer = False


if __name__ == "__main__":
    play_game()
