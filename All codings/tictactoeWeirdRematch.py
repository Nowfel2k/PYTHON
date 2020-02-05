                # --------------- Tic Tac Toe ------------------ #

# -- Global Variables --

# Board Creation
Board = ['-','-','-',
         '-','-','-',
         '-','-','-']

gameStillRunning = True

winner = ''


# -- Functions --

# Display
def Display():
    print("\n\t"+Board[0] +"|"+Board[1]+"|"+Board[2]+"\n"
          +"\t"+Board[3] +"|"+Board[4]+"|"+Board[5]+"\n"
          +"\t"+Board[6] +"|"+Board[7]+"|"+Board[8]+"\n")

# To Restart or not
def restartOrNot():
    global Board, gameStillRunning
    restart_decision = str(input("\nDo you want to restart the game? (Y/N) :"))
    if restart_decision == 'y':
        Board = ['-','-','-',
                 '-','-','-',
                 '-','-','-']
        winner = ''
        gameStillRunning = True
        StartGame()
    if (restart_decision == 'n'):
        exit()


# Turn of the X player
def xTurn():
    Display()
    try:
        choice = int(input("Enter X/O at 1-9 :"))
        choice -= 1
        if Board[choice] == 'X' or Board[choice] == 'O':
            print("Place occupied, Enter again.")
            xTurn()
        else:
            Board[choice] = 'X'
    except Exception as x_wrong:
        print(x_wrong)
        print("Wrong input, try again.")
        xTurn()
    return


# Turn of the O player
def oTurn():
    Display()
    try:
        choice = int(input("Enter X/O at 1-9 :"))
        choice -= 1
        if Board[choice] == 'X' or Board[choice] == 'O':
            print("Place occupied, Enter again.")
            oTurn()
        else:
            Board[choice] = 'O'
    except Exception as o_wrong:
        print(o_wrong)
        print("Wrong input, try again.")
        oTurn()
    return


# Check tie
def checkTie():
    global gameStillRunning
    # if (Board[0] == 'X' or 'O') and (Board[1]== 'X' or 'O') and (Board[2]== 'X' or 'O') and (Board[3]== 'X' or 'O') and (Board[4]== 'X' or 'O') and (Board[5]== 'X' or 'O') and (Board[6]== 'X' or 'O') and (Board[7]== 'X' or 'O') and (Board[8]== 'X' or 'O') and (Board[9]== 'X' or 'O'):
    if '-' not in Board:
        Display()
        print("\nThe match is now a TIE.")
        gameStillRunning = False
        restartOrNot()


# Check row - Sub Function of check_Winner
def check_row():
    global winner, gameStillRunning
    if (Board[0] == Board [1] == Board[2]) and (Board[1] != '-'):
            winner = Board[0]
            gameStillRunning = False
            declare_winner()
    if (Board[3] == Board [4] == Board[5]) and (Board[3] != '-'):
            winner = Board[3]
            gameStillRunning = False
            declare_winner()
    if (Board[6] == Board [7] == Board[8]) and (Board[6] != '-'):
            winner = Board[6]
            gameStillRunning = False
            declare_winner()


# Check column - Sub Function of check_Winner
def check_column():
    global winner, gameStillRunning
    if (Board[0] == Board [3] == Board[6]) and (Board[0] != '-'):
            winner = Board[0]
            gameStillRunning = False
            declare_winner()
    if (Board[1] == Board [4] == Board[7]) and (Board[1] != '-'):
            winner = Board[1]
            gameStillRunning = False
            declare_winner()
    if (Board[2] == Board [5] == Board[8]) and (Board[2] != '-'):
            winner = Board[2]
            gameStillRunning = False
            declare_winner()


# Check digonal - Sub Function of check_Winner
def check_diagonal():
    global winner, gameStillRunning
    if (Board[0] == Board [4] == Board[8]) and (Board[0] != '-'):
            winner = Board[0]
            gameStillRunning = False
            declare_winner()
    if (Board[6] == Board [4] == Board[2]) and (Board[6] != '-'):
            winner = Board[6]
            gameStillRunning = False
            declare_winner()


# Check winner
def check_winner():
    check_row()
    check_column()
    check_diagonal()
    return
    

# Declaring the Winner - End of the game
def declare_winner():
    if winner != '-':
        print("\n"+winner + " is the winner.")
        restartOrNot()


# Start Game - Main Game Manager
def StartGame():
    global gameStillRunning
    check_winner()
    checkTie()
    if gameStillRunning == True:
        xTurn()
    check_winner()
    checkTie()
    if gameStillRunning == True:
        oTurn()
    check_winner()
    checkTie()
    if gameStillRunning == True:
        StartGame()


StartGame()


                    #--------------- THE END ---------------#








