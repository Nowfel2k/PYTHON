from threading import *

class Book:
    def __init__(self, aTickets):
        self.aTickets = aTickets
        self.l = Semaphore()

    def buy(self, rTickets):
        self.l.acquire()
        print("Seats Available : ", self.aTickets)
        if self.aTickets >= rTickets:
            print("\nBooking...")
            print("Seats Available : ", self.aTickets)
            self.aTickets = self.aTickets - rTickets
        else:
            print("\nSeats Available : ", self.aTickets)
            print("All seats full.")
        self.l.release()


ClassObj = Book(10)
t1 = Thread(target=ClassObj.buy(2))
t2 = Thread(target=ClassObj.buy(3))
t3 = Thread(target=ClassObj.buy(6))
