# class Rectangle:
#   def __init__(self):
#     self.length = 10
#     self.breadth = 5

#   def area(self):
#     return self.length * self.breadth

#   def perimeter(self):
#     return 2 * (self.length + self.breadth)

# r = Rectangle()
# print("length: ",r.length) 
# print("breadth: ",r.breadth)
# print("Area: ",r.area())
# print("Perimeter: ",r.perimeter())  

#with parameters and arguments
class Rectangle:
  def __init__(self,l=1,b=2):
    self.length = l
    self.breadth = b

  def area(self):
    return self.length * self .breadth

  def perimeter(self):
    return 2 * (self.length + self.breadth)  
  

# r1 = Rectangle(8,6)
# r2 = Rectangle(5)
r3 = Rectangle()

print("length: ",r3.length) 
print("breadth: ",r3.breadth)
print("Area: ",r3.area())
print("Perimeter: ",r3.perimeter())  

