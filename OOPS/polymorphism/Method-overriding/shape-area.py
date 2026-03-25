class Shape:
  def area(self):
    print("calculating the area")

class Circle(Shape):
  def area(self):
    print("Area of the circle")

class Rectangle(Shape):
  def area(self):
    print("Area of the rectangle")

c = Circle ()
r = Rectangle()

c.area()
r.area()