
def UserEntry():
    count = 0
    id = 'Navfal'
    password = 'kappa'
    while count < 3:
        UserID = input("\nEnter the username : ")
        Pass = input("Enter Password : ")
        if UserID == id and Pass == password:
            print("\nLogin Successful")
            exit()
        else:
            if UserID != id and Pass == password:
                print("There is no account having this user-name.")
            elif UserID == id and Pass != password:
                print("Wrong Password")
            elif UserID != id and Pass != password:
                print("No account found")
        count += 1
    print("Out of Tries.")
    main()

def Giraffe():
    secret_word = "giraffe"
    guess = ""
    guess_count = 0
    out_of_guesses = False

    while guess != secret_word and not out_of_guesses:
        if guess_count < 3:
            guess = input("Enter a guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("You Lose!")
    else:
        print("You Win!")

def main():
    Giraffe()

UserEntry()







