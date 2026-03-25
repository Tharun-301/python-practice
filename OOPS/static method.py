class Rectangle:

  def __init__(self,l,b):
    self.length = l
    self.breadth = b
    
  @staticmethod
  def calc_area(length, breadth):
    return length * breadth

r1 = Rectangle(15,8)
print(Rectangle.calc_area(10,7))    