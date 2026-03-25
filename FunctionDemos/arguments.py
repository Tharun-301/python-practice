#positional Argument- pass in same order
def volume(length, breadth, height):

  print(length, breadth, height)
  vol = length * breadth * height
  return vol 

v = volume(5,4,3)
print(v)

# def volume(length, breadth, height):
#   vol = length * breadth * height
#   return vol
# length = int(input('Enter the length: '))
# breadth = int(input('Enter the breadth: '))
# height = int(input('Enter the height: '))
# v = volume(length,breadth,height)
# print(v)

#keyworD Argument- pass in any order
def volume(length, breadth, height):

  print(length, breadth, height)
  vol = length * breadth * height
  return vol 

v = volume(length=5,breadth=4,height=3)
#v = volume(height=3,length=5,breadth=4)
print(v)

#mixed arguments- either positional or keyword arguments, but not both
#                - positional on left and keyword on rigth
def volume(length, breadth, height):

  print(length, breadth, height)
  vol = length * breadth * height
  return vol 

v = volume(5,4,height=3)
print(v)