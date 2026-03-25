class Square:
  def __init__(self):#instance variables
    self.side = 6

  def area(self):#instance method
    return self.side * self.side

s = Square()
print("Area of square is:",s.area() )   

class Test():
  def __init__(self):
    self.a = 10

  def fun(self):
    self.b = 20

  def show(self):
    print(self.a)
    print(self.b)

t = Test()
t.fun()
t.c = 30 #we can create instance variables upon objects
t.show()        