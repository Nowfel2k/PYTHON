
def factorial(n):
    fact=1
    while(n>1):
        fact = fact * n
        n -=1
    if n<=1 :
        print(fact)
        n=int(input("\nEnter value of n :"))
        if n=="":
            print("Invalid input, try again")
        factorial(n)

n=int(input("\nEnter value of n :"))
if n=="":
    print("Invalid input, try again")
factorial(n)
