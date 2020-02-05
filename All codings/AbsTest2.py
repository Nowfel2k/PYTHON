from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP Scroll")
class HPNotebook(HP):
    def click(self):
        print("HP Click")

class DELL(TouchScreenLaptop):
    def scroll(self):
        print("DELL Scroll")
class DELLNotebook(DELL):
    def click(self):
        print("DELL Click")


HP_Note = HPNotebook()
DELL_Note = DELLNotebook()

HP_Note.click()
HP_Note.scroll()
DELL_Note.click()
DELL_Note.scroll()
