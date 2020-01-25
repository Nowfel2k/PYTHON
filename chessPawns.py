# IMPROPER CODE AT LINE 215
import os
import time

approve = False

board = [[2 , 2 , 2 , 2 , 2 , 2 , 0 ], 
        [ 2 , 2 , 2 , 2 , 2 , 2 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 1 , 1 , 1 , 1 , 1 , 1 , 0 ],
        [ 1 , 1 , 1 , 1 , 1 , 1 , 0 ]]


def displayBoard():
    print(" \t\t\t\t " , ' ' , '  | A | B | C | D | E | F |\n')
    print(" \t\t\t\t " , '1   |' , board[1][0] , "|" , board[1][1] , "|" , board[1][2] , "|" , board[1][3] , "|" , board[1][4] , "|" , board[1][5] , "|")
    print(" \t\t\t\t " , '2   |' , board[2][0] , "|" , board[2][1] , "|" , board[2][2] , "|" , board[2][3] , "|" , board[2][4] , "|" , board[2][5] , "|")
    print(" \t\t\t\t " , '3   |' , board[3][0] , "|" , board[3][1] , "|" , board[3][2] , "|" , board[3][3] , "|" , board[3][4] , "|" , board[3][5] , "|")
    print(" \t\t\t\t " , '4   |' , board[4][0] , "|" , board[4][1] , "|" , board[4][2] , "|" , board[4][3] , "|" , board[4][4] , "|" , board[4][5] , "|")
    print(" \t\t\t\t " , '5   |' , board[5][0] , "|" , board[5][1] , "|" , board[5][2] , "|" , board[5][3] , "|" , board[5][4] , "|" , board[5][5] , "|")
    print(" \t\t\t\t " , '6   |' , board[6][0] , "|" , board[6][1] , "|" , board[6][2] , "|" , board[6][3] , "|" , board[6][4] , "|" , board[6][5] , "|")



# GAME INTRO
def gameIntro():
    print(" \t\t\t ----------------------------")
    print(" \t\t\t WELCOME TO CHESS OF PAWNS ")
    print(" \t\t\t ----------------------------")
    print(" \n\n The first one to reach the enemy territory wins!")
    
    print(" \n Ready?")
    a = input('').split(" ")[0]
    print(a)
    
    os.system('cls')
    return

# DECLARE WINNER
def declareWinner(winner):
    os.system('cls')
    displayBoard()
    print("\n\t\t\t\t  #################################")
    print("\n\t\t\t\t\t" + winner + " is the winner")
    print("\n\t\t\t\t  #################################\n\n")

    exit()


# PLAYER 1 TURN
def firstTurn():
    

    displayBoard()
    print("\nPlayer 1 Turn")
    col, row = input("\nSelect a piece to move (like C6): ")
    row = int(row)

    # SETTING PROPER COORDINATES
    if (col == 'a' or col == 'A'): col = 0
    if (col == 'b' or col == 'B'): col = 1
    if (col == 'c' or col == 'C'): col = 2
    if (col == 'd' or col == 'D'): col = 3
    if (col == 'e' or col == 'E'): col = 4
    if (col == 'f' or col == 'F'): col = 5

    if (board[row][col] == 1):
        # FIRST POSSIBILITY
        def startPos():
            if(board[row + 1][col] != 1 and board[row - 1][col] != 2):
                board[row - 1][col] = 7
                board[row - 2][col] = 7

        # SECOND POSSIBILITY
        def forwardPos():
            if(board[row + 1][col] != 1 and board[row - 1][col] != 2):
                board[row - 1][col] = 7

        # CHECKING POSITION
        if (row == 6):
            startPos()
        else:
            forwardPos()

        # CHECKING FOR ENEMY PAWNS NEARBY
        if (board[row - 1][col - 1] == 2):
            board[row - 1][col - 1] = 7
        if (board[row - 1][col + 1] == 2):
            board[row - 1][col + 1] = 7

        approve = False

        # MOVING THE PIECE
        os.system('cls')
        displayBoard()
        col1, row1 = input(" \n Where to move the piece? ")
        if (col1 == 'a' or col1 == 'A'): col1 = 0
        if (col1 == 'b' or col1 == 'B'): col1 = 1
        if (col1 == 'c' or col1 == 'C'): col1 = 2
        if (col1 == 'd' or col1 == 'D'): col1 = 3
        if (col1 == 'e' or col1 == 'E'): col1 = 4
        if (col1 == 'f' or col1 == 'F'): col1 = 5
        col1 = int(col1)
        row1 = int(row1)

        # SEVENS ARE THE POSSIBLE PLACES TO MOVE TO
        if (board[row1][col1] == 7):
            board[row1][col1] = 1
            board[row][col] = 0
            approve = True
        else:
            print("Cannot move piece to this position, try again")
            time.sleep(1)
            os.system('cls')
            secondTurn()

        # CLEANING ALL THE SEVENS OF THE BOARD
        if board[row - 1][col - 1] == 7: board[row - 1][col - 1] = 2
        if board[row - 1][col + 1] == 7: board[row - 1][col + 1] = 2
        if board[row - 1][col] == 7: board[row - 1][col] = 0
        if board[row - 2][col] == 7: board[row - 2][col] = 0

        # CHECK IF PIECE REACHED ENEMY TERRITORY
        if row1 == 1 and approve == True:
            winner = "Player 1"
            declareWinner(winner)


    else:
        print("Invalid input, try again")
        time.sleep(1)
        os.system('cls')
        firstTurn()

    os.system('cls')
    return




# PLAYER 2 TURN
def secondTurn():
    
    displayBoard()
    print("\nPlayer 2 Turn")
    col, row = input(" \n Select a piece to move (like D1): ")
    row = int(row)

    # SETTING PROPER COORDINATES
    if (col == 'a' or col == 'A'): col = 0
    if (col == 'b' or col == 'B'): col = 1
    if (col == 'c' or col == 'C'): col = 2
    if (col == 'd' or col == 'D'): col = 3
    if (col == 'e' or col == 'E'): col = 4
    if (col == 'f' or col == 'F'): col = 5

    
    if (board[row][col] == 2):
        # FIRST POSSIBILITY
        def startPos():
            if(board[row + 1][col] != 1 and board[row + 1][col] != 2):
                board[row + 1][col] = 7
                board[row + 2][col] = 7

        # SECOND POSSIBILITY
        def forwardPos():
            if(board[row + 1][col] != 1 and board[row + 1][col] != 2):
                board[row + 1][col] = 7

        # CHECKING POSITION
        if (row == 1):
            startPos()
        else:
            forwardPos()

        # CHECKING FOR ENEMY PAWNS NEARBY
        if (board[row + 1][col - 1] == 1):
            board[row + 1][col - 1] = 7
        if (board[row + 1][col + 1] == 1):
            board[row + 1][col + 1] = 7

        approve = False

        # MOVING THE PIECE
        os.system('cls')
        displayBoard()
        col2, row2 = input(" \n Where to move the piece? ")
        if (col2 == 'a' or col2 == 'A'): col2 = 0
        if (col2 == 'b' or col2 == 'B'): col2 = 1
        if (col2 == 'c' or col2 == 'C'): col2 = 2
        if (col2 == 'd' or col2 == 'D'): col2 = 3
        if (col2 == 'e' or col2 == 'E'): col2 = 4
        if (col2 == 'f' or col2 == 'F'): col2 = 5
        col2 = int(col2)
        row2 = int(row2)

        # SEVENS ARE THE POSSIBLE PLACES TO MOVE TO
        if (board[row2][col2] == 7):
            board[row2][col2] = 2
            board[row][col] = 0
            approve = True
        else:
            print("Cannot move piece to this position, try again")
            time.sleep(1)
            os.system('cls')
            secondTurn()


        # CLEANING ALL THE SEVENS OFF THE BOARD
        if board[row + 1][col - 1] == 7: board[row + 1][col - 1] = 1
        if board[row + 1][col + 1] == 7: board[row + 1][col + 1] = 1
        
        # PROBLEMATIC RESULT - PLAYER 2 PAWNS KILL P1 PAWNS OF SAME COLUMN
        # if board[row + 1][col] == 7: board[row + 1][col] = 0
        # if board[row + 2][col] == 7: board[row + 2][col] = 0


        # CHECK IF PIECE REACHED ENEMY TERRITORY
        if row2 == 6 and approve == True:
            winner = "Player 2"
            declareWinner(winner)


    else:
        print("Invalid input, try again")
        time.sleep(1)
        os.system('cls')
        secondTurn()
        return

    os.system('cls')
    return



# GAME MAIN MANAGER
def startGame():
    firstTurn()
    secondTurn()
    startGame()
    return


# START THE GAME BY CALLING THE FUNCTIONS
gameIntro()
startGame()
