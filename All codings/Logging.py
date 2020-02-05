try:
    password = input("Enter Password (min 8 characters) : ")
    assert(len(password)>7)

except AssertionError as A:
    print("Password is too short")
else:
    print("Password Accepted")


