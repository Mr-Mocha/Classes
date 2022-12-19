import random

class Car:
    # Attributes
    engineType = ""
    horsePower = ""
    numOfDoors = 0
    brand = ""
    model = ""
    vehicleType = ""
    color = ""

    # Methods
    # Drive, Reverse, Turn, Start, Stop
    def __init__(self,brand,model,doors):
        self.brand = brand
        self.model = model
        self.numOfDoors = doors

    def Drive(self):
        print(f"Car is moving at {random.randint(50,100)}mph")

    def Start(self):
        print(f"{self.brand} {self.model} has been started")

    def PickColor(self):
        color = input("Pick a color for your car:  ")
        self.color = color

# Object of Car class
myCar = Car ("Mitsubishi","Eclipse", 4)
AjCar = Car ("Honda","Civic", 2)

myCar.PickColor()
print(f"The color of your car is {myCar.color}")
myCar.Start()
myCar.Drive()
print(f"My car has {myCar.numOfDoors} doors")

AjCar.Start()
AjCar.Drive()
print(f"My car has {AjCar.numOfDoors} doors")