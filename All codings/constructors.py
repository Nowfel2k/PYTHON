class Construct:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def length(self):
        len_of_name = len(self.name)
        print(len_of_name)


a = Construct('Michael Scott', 30)
print(a._Construct__id)

