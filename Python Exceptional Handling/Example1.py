#try and except -  block
# a,b = 10,0

# try:
#   c = a//b
#   print(c)
# except:
#   print("b should not divide with a")

# print("End of program")

# #TypeError: list indices must be integers or slices, not str
# l = [10,20,30,40,50]

# index = 'abc'
# print(l[index])
# print("End of program")

# #IndexError: list index out of range
l = [10,20,30,40,50]
try:
  index = 9 #if index-3 is given it will excute try block  
  print(l[index])
  print("End of try")
except:
  print("Invalid Index")  
print("End of program")