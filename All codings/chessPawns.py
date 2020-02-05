# CODE NEEDS IMPROVEMENT AT LINE 305
import os
import time

condition = 1

player1 = ''
player2 = ''

approve = False

board = [
        ['P2' , 'P2' , 'P2' , 'P2' , 'P2' , 'P2' , '  ' ], 
        ['P2' , 'P2' , 'P2' , 'P2' , 'P2' , 'P2' , '  ' ],
        [ '  ' , '  ' , '  ' , '  ' , '  ' , '  ' , '  ' ],
        [ '  ' , '  ' , '  ' , '  ' , '  ' , '  ' , '  ' ],
        [ '  ' , '  ' , '  ' , '  ' , '  ' , '  ' , '  ' ], 
        [ '  ' , '  ' , '  ' , '  ' , '  ' , '  ' , '  ' ],
        [ 'P1' , 'P1' , 'P1' , 'P1' , 'P1' , 'P1' , '  ' ],
        [ 'P1' , 'P1' , 'P1' , 'P1' , 'P1' , 'P1' , '  ' ]
        ]


def displayBoard():
    print(" \t\t\t\t " , ' ', '  | A  | B  | C  |  D |  E |  F |\n')
    print(" \t\t\t\t " , '1   |' , board[1][0] , "|" , board[1][1] , "|" , board[1][2] , "|" , board[1][3] , "|" , board[1][4] , "|" , board[1][5] , "|")
    print(" \t\t\t\t " , '2   |' , board[2][0] , "|" , board[2][1] , "|" , board[2][2] , "|" , board[2][3] , "|" , board[2][4] , "|" , board[2][5] , "|")
    print(" \t\t\t\t " , '3   |' , board[3][0] , "|" , board[3][1] , "|" , board[3][2] , "|" , board[3][3] , "|" , board[3][4] , "|" , board[3][5] , "|")
    print(" \t\t\t\t " , '4   |' , board[4][0] , "|" , board[4][1] , "|" , board[4][2] , "|" , board[4][3] , "|" , board[4][4] , "|" , board[4][5] , "|")
    print(" \t\t\t\t " , '5   |' , board[5][0] , "|" , board[5][1] , "|" , board[5][2] , "|" , board[5][3] , "|" , board[5][4] , "|" , board[5][5] , "|")
    print(" \t\t\t\t " , '6   |' , board[6][0] , "|" , board[6][1] , "|" , board[6][2] , "|" , board[6][3] , "|" , board[6][4] , "|" , board[6][5] , "|")



# GAME INTRO
def gameIntro():
    os.system('cls')
    print(" \t\t\t ----------------------------")
    print(" \t\t\t WELCOME TO CHESS OF PAWNS ")
    print(" \t\t\t ----------------------------")
    print(" \n\n The first one to reach the enemy territory wins!")
    
    # LIKE GETCHAR() IN C LANGUAGE
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
    global player1, player2

    colNum, rowNum = 0, 0

    displayBoard()
    print("\n" + player1 + " Turn")

    try:
        col, row = input(" \n Select a piece to move (like D1): ")

    except ValueError:
        print(" \n Try again")
        time.sleep(2)
        os.system('cls')
        firstTurn()    
        return
    
    
    rowNum = int(row)

    # SETTING PROPER COORDINATES
    if (col == 'a' or col == 'A'): colNum = 0
    if (col == 'b' or col == 'B'): colNum = 1
    if (col == 'c' or col == 'C'): colNum = 2
    if (col == 'd' or col == 'D'): colNum = 3
    if (col == 'e' or col == 'E'): colNum = 4
    if (col == 'f' or col == 'F'): colNum = 5

    if (board[rowNum][colNum] == 'P1'):
        # FIRST POSSIBILITY
        def startPos():
            if(board[rowNum - 1][colNum] != 'P1' and board[rowNum - 1][colNum] != 'P2'):
                board[rowNum - 1][colNum] = 'C '
            if(board[rowNum - 2][colNum] != 'P1' and board[rowNum - 2][colNum] != 'P2'):
                board[rowNum - 2][colNum] = 'C '

        # SECOND POSSIBILITY
        def forwardPos():
            if(board[rowNum - 1][colNum] != 'P1' and board[rowNum - 1][colNum] != 'P2'):
                board[rowNum - 1][colNum] = 'C '

        # CHECKING POSITION
        if (rowNum == 6):
            startPos()
        else:
            forwardPos()

        # CHECKING FOR ENEMY PAWNS NEARBY
        if (board[rowNum- 1][colNum - 1] == 'P2'):
            board[rowNum- 1][colNum - 1] = 'C '
        if (board[rowNum- 1][colNum + 1] == 'P2'):
            board[rowNum- 1][colNum + 1] = 'C '

        approve = False

        # MOVING THE PIECE
        os.system('cls')
        displayBoard()

        moveCol, moveRow = 0, 0

        try:
            col1, row1 = input(" \n Where to move the piece? ")
        except ValueError: 
            print(" \n Invalid Input")
            time.sleep(2)
            os.system('cls')

            if board[rowNum- 1][colNum - 1] == 'C ': board[rowNum- 1][colNum - 1] = 'P2'
            if board[rowNum- 1][colNum + 1] == 'C ': board[rowNum- 1][colNum + 1] = 'P2'
            if board[rowNum- 1][colNum ] == 'C ': board[rowNum- 1][colNum ] = '  '
            if board[rowNum- 2][colNum ] == 'C ': board[rowNum- 2][colNum ] = '  '

            firstTurn()
            return

        
        if (col1 == 'a' or col1 == 'A'): moveCol = 0
        if (col1 == 'b' or col1 == 'B'): moveCol = 1
        if (col1 == 'c' or col1 == 'C'): moveCol = 2
        if (col1 == 'd' or col1 == 'D'): moveCol = 3
        if (col1 == 'e' or col1 == 'E'): moveCol = 4
        if (col1 == 'f' or col1 == 'F'): moveCol = 5
        moveCol = int(moveCol)
        moveRow = int(row1)

        # SEVENS ARE THE POSSIBLE PLACES TO MOVE TO
        if (board[moveRow][moveCol] == 'C '):
            board[moveRow][moveCol] = 'P1'
            board[rowNum][colNum ] = '  '
            approve = True
        else:
            print("Cannot move piece to this position, try again")
            time.sleep(2)
            os.system('cls')

            if board[rowNum- 1][colNum - 1] == 'C ': board[rowNum- 1][colNum - 1] = 'P2'
            if board[rowNum- 1][colNum + 1] == 'C ': board[rowNum- 1][colNum + 1] = 'P2'
            if board[rowNum- 1][colNum ] == 'C ': board[rowNum- 1][colNum ] = '  '
            if board[rowNum- 2][colNum ] == 'C ': board[rowNum- 2][colNum ] = '  '

            firstTurn()
            return


        # CLEANING ALL THE SEVENS OF THE BOARD
        if board[rowNum- 1][colNum - 1] == 'C ': board[rowNum- 1][colNum - 1] = 'P2'
        if board[rowNum- 1][colNum + 1] == 'C ': board[rowNum- 1][colNum + 1] = 'P2'
        if board[rowNum- 1][colNum ] == 'C ': board[rowNum- 1][colNum ] = '  '
        if board[rowNum- 2][colNum ] == 'C ': board[rowNum- 2][colNum ] = '  '

        # CHECK IF PIECE REACHED ENEMY TERRITORY
        if moveRow == 1 and approve == True:
            declareWinner(player1)


    else:
        print("Invalid input, try again")
        time.sleep(2)
        os.system('cls')
        firstTurn()
        return

    os.system('cls')
    return




# PLAYER 2 TURN
def secondTurn():
    global player1, player2

    colNum, rowNum = 0, 0

    displayBoard()
    print("\n" + player2 + " Turn")

    try:
        col, row = input(" \n Select a piece to move (like D1): ")

    except ValueError:
        print(" \n Try again")
        time.sleep(2)
        os.system('cls')
        secondTurn()
        return


    rowNum = int(row)

    # SETTING PROPER COORDINATES
    if (col == 'a' or col == 'A'): colNum = 0
    if (col == 'b' or col == 'B'): colNum = 1
    if (col == 'c' or col == 'C'): colNum = 2
    if (col == 'd' or col == 'D'): colNum = 3
    if (col == 'e' or col == 'E'): colNum = 4
    if (col == 'f' or col == 'F'): colNum = 5

    
    if (board[rowNum][colNum] == 'P2'):
        
        # FIRST POSSIBILITY
        def startPos():
            if(board[rowNum + 1][colNum] != 'P1' and board[rowNum + 1][colNum] != 'P2'):
                board[rowNum + 1][colNum] = 'C '
                board[rowNum + 2][colNum] = 'C '

        # SECOND POSSIBILITY
        def forwardPos():
            if(board[rowNum + 1][colNum] != 'P1' and board[rowNum + 1][colNum] != 'P2'):
                board[rowNum + 1][colNum] = 'C '

        # CHECKING POSITION
        if (rowNum == 1):
            startPos()
        else:
            forwardPos()

        # CHECKING FOR ENEMY PAWNS NEARBY
        if (board[rowNum + 1][colNum - 1] == 'P1'):
            board[rowNum + 1][colNum - 1] = 'C '
        if (board[rowNum + 1][colNum + 1] == 'P1'):
            board[rowNum + 1][colNum + 1] = 'C '

        approve = False

        # MOVING THE PIECE
        os.system('cls')
        displayBoard()

        moveCol, moveRow = 0, 0

        try:
            col2, row2 = input(" \n Where to move the piece? ")
        except ValueError:
            print(" \n Invalid Input")
            time.sleep(2)
            os.system('cls')

            if board[rowNum- 1][colNum - 1] == 'C ': board[rowNum- 1][colNum - 1] = 'P2'
            if board[rowNum- 1][colNum + 1] == 'C ': board[rowNum- 1][colNum + 1] = 'P2'
            if board[rowNum- 1][colNum ] == 'C ': board[rowNum- 1][colNum ] = '  '
            if board[rowNum- 2][colNum ] == 'C ': board[rowNum- 2][colNum ] = '  '

            secondTurn()
            return
        
        
        if (col2 == 'a' or col2 == 'A'): moveCol = 0
        if (col2 == 'b' or col2 == 'B'): moveCol = 1
        if (col2 == 'c' or col2 == 'C'): moveCol = 2
        if (col2 == 'd' or col2 == 'D'): moveCol = 3
        if (col2 == 'e' or col2 == 'E'): moveCol = 4
        if (col2 == 'f' or col2 == 'F'): moveCol = 5
        moveCol = int(moveCol)
        moveRow = int(row2)

        # SEVENS ARE THE POSSIBLE PLACES TO MOVE TO
        if (board[moveRow][moveCol] == 'C '):
            board[moveRow][moveCol] = 'P2'
            board[rowNum][colNum] = '  '
            approve = True
        else:
            print("Cannot move piece to this position, try again")
            time.sleep(2)
            os.system('cls')

            if board[rowNum- 1][colNum - 1] == 'C ': board[rowNum- 1][colNum - 1] = 'P2'
            if board[rowNum- 1][colNum + 1] == 'C ': board[rowNum- 1][colNum + 1] = 'P2'
            if board[rowNum- 1][colNum ] == 'C ': board[rowNum- 1][colNum ] = '  '
            if board[rowNum- 2][colNum ] == 'C ': board[rowNum- 2][colNum ] = '  '

            secondTurn()
            return


        # CLEANING ALL THE SEVENS OFF THE BOARD
        if board[rowNum + 1][colNum - 1] == 'C ': board[rowNum + 1][colNum - 1] = 'P1'
        if board[rowNum + 1][colNum + 1] == 'C ': board[rowNum + 1][colNum + 1] = 'P1'
        # PLAYER 2 PAWNS KILLS STRAIGHT P1 PAWNS
        if board[rowNum + 1][colNum] == 'C ': board[rowNum + 1][colNum] = '  '
        if board[rowNum + 2][colNum] == 'C ': board[rowNum + 2][colNum] = '  '


        # CHECK IF PIECE REACHED ENEMY TERRITORY
        if moveRow == 6 and approve == True:
            declareWinner(player2)


    else:
        print("Invalid input, try again")
        time.sleep(2)
        os.system('cls')
        secondTurn()
        return

    os.system('cls')
    return





# GAME MAIN MANAGER
def startGame():
    global player1, player2, condition

    while(condition):
        player1 = input("Enter player 1 name : ")
        player2 = input("Enter player 2 name : ")
        condition = 0

    firstTurn()
    secondTurn()
    startGame()
    return




# START THE GAME BY CALLING THE FUNCTIONS
gameIntro()
startGame()
