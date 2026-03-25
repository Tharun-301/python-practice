#one try block can have multiple exceptions block and one exception block can have multiple exceptions or variable names 
# L = [10,20,30,40,50]

# try:
#   index = int("abc") #9,"abc",int(abc)
#   print(L[index])
# except IndexError:
#   print("Index value error")
# except TypeError:
#   print('Index should be int')  
# except:
#   print("some error") 

# print("End of program1")


L = ["a",'b','c','d','e']

try:
  index = "abc" #9,"abc",int(abc)
  print(L[index])
except IndexError as msg:
  print(msg)
except TypeError as msg1:
  print(msg1) 
except ValueError as msg2:
  print(msg2)    

print('End of program2')


#Instead of writing two except block we can write a single except block that can handle both the exception
L = [10,20,30,40,50]

try:
  index = int(input('Enter the index: '))#9,"abc",int(abc)
  print(L[index])
except (IndexError,ValueError) as msg:
  print(msg)

print("End of program3")
