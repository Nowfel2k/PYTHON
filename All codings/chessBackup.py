import os
import time

p1 = ""
p2 = ""

approve = False

board = [[ 2 , 2 , 2 , 2 , 2 , 2 ],\
        [ 2 , 2 , 2 , 2 , 2 , 2 ],\
        [ '-' , '-' , '-' , '-' , '-' , '-' ],\
        [ '-' , '-' , '-' , '-' , '-' , '-' ],\
        [ '-' , '-' , '-' , '-' , '-' , '-' ],\
        [ '-' , '-' , '-' , '-' , '-' , '-' ],\
        [ 1 , 1 , 1 , 1 , 1 , 1 ]]

def displayBoard():
    print(" \t\t\t\t " + ' ' + ' |A|B|C|D|E|F|  ')
    print(" \t\t\t\t " + '1 |' + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|" + board[1][3] + "|" + board[1][4] + "|" + board[1][5] + "|")
    print(" \t\t\t\t " + '2 |' + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|" + board[2][3] + "|" + board[2][4] + "|" + board[2][5] + "|")
    print(" \t\t\t\t " + '3 |' + board[3][0] + "|" + board[3][1] + "|" + board[3][2] + "|" + board[3][3] + "|" + board[3][4] + "|" + board[3][5] + "|")
    print(" \t\t\t\t " + '4 |' + board[4][0] + "|" + board[4][1] + "|" + board[4][2] + "|" + board[4][3] + "|" + board[4][4] + "|" + board[4][5] + "|")
    print(" \t\t\t\t " + '5 |' + board[5][0] + "|" + board[5][1] + "|" + board[5][2] + "|" + board[5][3] + "|" + board[5][4] + "|" + board[5][5] + "|")
    print(" \t\t\t\t " + '6 |' + board[6][0] + "|" + board[6][1] + "|" + board[6][2] + "|" + board[6][3] + "|" + board[6][4] + "|" + board[6][5] + "|")


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

    p1 = input("Enter player 1 name : ")
    p2 = input("Enter player 2 name : ")
    time.sleep(2)
    os.system('cls')
    
    return

# DECLARE WINNER
def declareWinner(winner):
    print(winner + " is the winner")
    exit()


# PLAYER 1 TURN
def firstTurn():
    displayBoard()
    if p1 != "": print(p1 + "'s turn")
    col, row = input(" \n Select a piece to move (like C6): ")
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
            board[row - 1][col] = 0
            board[row - 2][col] = 0

        # SECOND POSSIBILITY
        def forwardPos():
            if(board[row - 1][col] != 2):
                board[row - 1][col] = 0

        # CHECKING POSITION
        if (row == 6):
            startPos()
        else:
            forwardPos()

        # CHECKING FOR ENEMY PAWNS NEARBY
        if (board[row - 1][col - 1] == 2):
            board[row - 1][col - 1] = 0
        if (board[row - 1][col + 1] == 2):
            board[row - 1][col + 1] = 0

        approve = False

        # MOVING THE PIECE
        col1, row1 = input(" \n Where to move the piece? ")
        if (board[row1][col1] == 0):
            board[row1][col1] = 1
            board[row][col] = '-'
            approve = True

        if row1 == 1 and approve == True:
            declareWinner(p1)


    else:
        print("Invalid input, try again")
        time.sleep(1)
        os.system('cls')
        firstTurn()

    time.sleep(2)
    os.system('cls')
    return




# PLAYER 2 TURN
def secondTurn():
    displayBoard()
    if p1 != "": print(p2 + "'s turn")
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
            board[row + 1][col] = 0
            board[row + 2][col] = 0

        # SECOND POSSIBILITY
        def forwardPos():
            if (board[row + 1][col] != 1):
                board[row + 1][col] = 0

        # CHECKING POSITION
        if (row == 1):
            startPos()
        else:
            forwardPos()

        # CHECKING FOR ENEMY PAWNS NEARBY
        if (board[row + 1][col - 1] == 1):
            board[row + 1][col - 1] = 0
        if (board[row + 1][col + 1] == 1):
            board[row + 1][col + 1] = 0

        approve = False

        # MOVING THE PIECE
        col1, row1 = input(" \n Where to move the piece? ")
        if(board[row1][col1] == 0):
            board[row1][col1] = 1
            board[row][col] = '-'
            approve = True

        if row1 == 6 and approve==True:
            declareWinner(p2)



    else:
        print("Invalid input, try again")
        secondTurn()

    time.sleep(2)
    os.system('cls')
    return



# GAME MAIN MANAGER
def startGame():
    
    firstTurn()
    secondTurn()
    startGame()
    return


# CALLING FUNCTIONS
gameIntro()
startGame()
