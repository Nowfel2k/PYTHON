class InvalidPasswordException(Exception):
    def __init__(self):
        pass

try:
    password = input("Enter Password (min 8 characters) : ")
    if len(password)<8:
        raise InvalidPasswordException()
    else:
        print("Password Accepted")

except InvalidPasswordException:
    print("Password too short")

