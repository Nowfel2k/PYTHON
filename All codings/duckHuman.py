class duck:
    def talk(self):
        print("Quack")

class human:
    def talk(self):
        print("Hello")

def callTalk(obj):
    obj.talk()

d = duck()
h = human()

callTalk(d)
callTalk(h)

def test():
    if __name__ == '__main__':
        return ("Function inside main python file")
    else:
        return ("Imported Function from module")

print(test())
