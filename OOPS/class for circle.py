import math 
class Circle:
  def __init__(self,radius):
    self.radius =  radius

  def area(self):
    return math.pi * self.radius ** 2  
  
  def perimeter(self):
    return 2 * math.pi * self.radius

radius = float(input('Enter the Radius: '))

c1 = Circle(radius)
print(f"Area of circle: {c1.area():.2f}")
print(f"Perimeter of circle: {c1.perimeter():.2f}")
