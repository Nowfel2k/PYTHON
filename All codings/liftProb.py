import time

# Global Variables
currentFloor = 0
firstLift = 3
secondLift = 5
thirdLift = 4


# Functions

# Travel Function for pressing 1
def travel():
    global currentFloor, firstLift, secondLift, thirdLift
    
    gotoFloor = int(input("\nWhich floor would you like to go to?  \nFloor number (0-10) : "))
    newDelayTime = gotoFloor - currentFloor


    test1 = int(firstLift - currentFloor)
    if (test1 < 0): test1 *= -1

    test2 = int(secondLift - currentFloor)
    if (test2 < 0): test2 *= -1

    test3 = int(thirdLift - currentFloor)
    if (test3 < 0): test3 *= -1



    if ((test1 < test2) and (test1 < test3)):
        print("\n1st Lift is Arriving\n")
        print("\n Please wait...\n")
        delayTime = firstLift - currentFloor

        if (delayTime < 0): delayTime *= -1
        time.sleep(delayTime)
        liftUsed = 1
        firstLift = currentFloor
        print("\n1st Lift has arrived to", currentFloor, " Floor")


    elif(test2 < test1) and (test2 < test3):
        print("\n2nd Lift is Arriving\n")
        print("\n Please wait...\n")
        delayTime = secondLift - currentFloor

        if (delayTime < 0): delayTime *= -1
        time.sleep(delayTime)

        liftUsed = 2
        secondLift = currentFloor
        print("\n2nd Lift has arrived to", currentFloor, " Floor")



    elif(test3 < test1) and (test3 < test2):
        print("\n3rd Lift is Arriving\n")
        print("\n Please wait...\n")
        delayTime = thirdLift - currentFloor

        if (delayTime < 0): delayTime *= -1
        time.sleep(delayTime)
        liftUsed = 3
        secondLift = currentFloor
        print("\n3rd Lift has arrived to",currentFloor," Floor")



    else:
        print("\n1st Lift is Close\n")
        print("\n Please wait...\n")
        delayTime = firstLift - currentFloor

        if (delayTime < 0): delayTime *= -1
        time.sleep(delayTime)
        liftUsed = 1
        firstLift = currentFloor
        print("\n1st Lift has arrived to", currentFloor, " Floor")



    if(liftUsed == 1):
        currentFloor = gotoFloor
        firstLift = gotoFloor
    elif(liftUsed == 2):
        currentFloor = gotoFloor
        secondLift = gotoFloor
    elif(liftUsed == 3):
        currentFloor = gotoFloor
        thirdLift = gotoFloor
    else:
        print("\nInvalid processing\n")

    print("\n")
    print("\nGoing to floor number ", gotoFloor, " Floor")
    if (newDelayTime < 0): newDelayTime *= -1
    time.sleep(newDelayTime)
    print("\nYou have arrived to the",currentFloor," Floor")
    time.sleep(3)
    Main()




# States the current floor you are at
def checkFloor():
    global currentFloor
    print("You are on floor number : ", currentFloor)
    time.sleep(3)
    Main()




# Displays lift positions
def checkLiftPositions():
    global firstLift, secondLift, thirdLift
    print("First Lift Position : ", firstLift)
    print("Second Lift Position : ", secondLift)
    print("Third Lift Position : ", thirdLift)
    time.sleep(3)
    Main()




# Lifts change positions after while working in office
def liftChangePositions():
    global firstLift, secondLift, thirdLift
    temp = firstLift + 1
    firstLift = secondLift + 1
    secondLift = thirdLift + 1
    thirdLift = temp

    if (firstLift >= 13):
        firstLift = firstLift % 12

    if (secondLift >= 13):
        secondLift = secondLift % 12

    if (thirdLift >= 13):
        thirdLift = thirdLift % 12


    time.sleep(3)
    Main()



# Main Driver of the Program
def Main():
    choice = int(input("\n\nWhat would you like to do?\
                    \nPress 1 to travel \nPress 2 to check the currentFloor\
                    \nPress 3 to check the Lift Positions \nPress 4 to work in office\
                    \nPress 5 to exit console\n\n"))
    if choice == 1:
        travel()
    elif choice == 2:
        checkFloor()
    elif choice == 3:
        checkLiftPositions()
    elif choice == 4:
        liftChangePositions()
    elif choice == 5:
        exit()
    else:
        print("Invalid Choice")
        Main()



# Starts the Program Execution
Main()


