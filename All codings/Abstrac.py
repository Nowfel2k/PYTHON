from abc import ABC, abstractmethod

class TouchScreenLaptop(ABC):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):
    def __init__(self, scroll, name, model):
        super().__init__(name, model)
        self.scroll = scroll

    def scroll(self):
        print("HP Scroll")

class DELL(TouchScreenLaptop):
    def __init__(self, scroll, name, model):
        super().__init__(name, model)
        self.scroll = scroll

    def scroll(self):
        print("DELL Scroll")

hp_lap = HP("HP Scroll", "HP Notebook", 2300)
dell_lap = DELL("DELL Scroll", "DELL Notebook", 4900)




