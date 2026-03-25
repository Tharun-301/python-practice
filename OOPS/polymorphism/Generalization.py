# Combining common features of multiple classes into a single parent class.
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# creating objects
d = Dog()
c = Cat()

# calling method
d.eat()
c.eat()