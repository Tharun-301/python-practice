# Creating more specific classes from a general parent class.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def doors(self):
        print("Car has 4 doors")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

c = Car()
b = Bike()

c.start()
c.doors()
b.wheels()



