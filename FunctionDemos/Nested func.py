def outer():

  def inner():
    print('Inner func')

  print('Outer func')  
  inner()

outer()

#Rectangle
def totalarea(l,b,h):

  def area(d1,d2):
    return d1 * d2
  
  return 2*(area(l,b)+area(b,h)+area(l,h))


print("Rectangle: ",totalarea(10,5,3))