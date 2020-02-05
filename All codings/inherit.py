class Car:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display(self):
        print("The name is", self.name, "and its used for :", self.type)


class Bike(Car):
    def __init__(self, name, type, Mileage):
        Car.__init__(self, name, type)
        self.Mileage = Mileage

b = Bike("Suzuki", "Racer", 25)
print(b.type)
print(b.display())

c= Car("Innova", "Casual")
print(c.type)

x = "TITLE"
print(x.title())

import duckHuman
print(duckHuman.test())
