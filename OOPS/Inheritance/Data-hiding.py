print("======= Public - can modify the data ========")
class Parent:
  
  def __init__(self,d):
    self.data = d

  def show(self):
    print(self.data)

p = Parent(10)
p.show()    
p.data = 20
p.show()
p.data = 150
p.show()

print("======= Private - The data won't change until keeping '__' ========")
#When we use "__" for properties they are not accessible by child classes and objects also
class Parent:
  
  def __init__(self,d):
    self.__data = d

  def show(self):
    print(self.__data)

p = Parent(10)
p.show()    
p.__data = 20
p.show()
p._Parent__data = 50  #Name Mangling - we can access by keeping _ to the class name
p.show()


print("======= Protected - It define by '_' ========")
class Parent:
  
  def __init__(self,d):
    self._data = d

  def show(self):
    print(self._data)

class Child(Parent):

  def __init__(self,d):
    super().__init__(d)

  def display(self):
    print(self._data)

c = Child(25)
c.show()
c.display()    


