class Rectangle:
  count = 0

  def __init__(self,l,b):
    self.length = l
    self.breadth = b
    Rectangle.count += 1   #class variables are used as shared data for all the instances of class.

  def area(self):
    return self.length * self.breadth

  def perimeter(self):
    return 2 * (self.length + self.breadth)
  
  @classmethod # without classmethod it treated as instance method, we use class name in object.
  def get_count(cls):
    return cls.count

r = Rectangle(15,7)
print("length: ",r.length) 
print("breadth: ",r.breadth)
print("Area: ",r.area())
print("Perimeter: ",r.perimeter())
print("count: ",Rectangle.get_count())

print("<-------   ------>")
r1 = Rectangle(8,3)
print("length: ",r1.length) 
print("breadth: ",r1.breadth)
print("Area: ",r1.area())
print("Perimeter: ",r1.perimeter())
print("count: ",Rectangle.get_count())

print("<-------   ------>")
r2 = Rectangle(12,5)
print("length: ",r2.length) 
print("breadth: ",r2.breadth)
print("Area: ",r2.area())
print("Perimeter: ",r2.perimeter())
print("count: ",Rectangle.get_count())