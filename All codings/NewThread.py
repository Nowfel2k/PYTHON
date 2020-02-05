from threading import Thread


def oddDisplay():
    i = 0
    print("Thread 1")
    while i <= 100:
        if i % 3 == 0:
            print(i)
        i += 1


def evenDisplay():
    i = 0
    print("Thread 2")
    while i <= 100:
        if i % 2 == 0:
            print(i)
        i += 1


# Main Thread
t1 = Thread(target=oddDisplay())
t2 = Thread(target=evenDisplay())

t1.start()
t2.start()
