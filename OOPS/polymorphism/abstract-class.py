# An abstract class is a class that cannot be instantiated (creating an object from a class) and contains abstract methods that must be implemented by its subclasses.
from abc import ABC, abstractmethod

class Shape:
  @abstractmethod
  def area():
    pass

class Circle(Shape):
  def area(self):
    print("area of circle")

class Rectangle(Shape):
  def area(self):
    print("area of rectangle")

# Objects can be created for child classes, not for the abstract class.
c = Circle()
r = Rectangle() 

c.area()
r.area()





