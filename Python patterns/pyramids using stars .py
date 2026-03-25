#half pyramid
print("----half pyramid----")
rows = 5
for i in range(1, rows + 1):
  for j in range(i):
    print("*",end = " ")
  print()  

#Inverted half pyramid
print("----Inverted half pyramid----")
rows = 5
for i in range(rows, 0 , -1):
  for j in range(i):
    print("*",end=" ")
  print()  

#full pyramid
print("----full pyramid----")
rows = 5
for i in range(1, rows + 1):
  for j in range(rows-i):
    print(" ", end=" ")

  for k in range(2 * i - 1):
    print("*", end = " ")
  print()   


# Inverted full pyramid
print("-----Inverted full pyramid-----")
rows = 5
for i in range(rows,0,-1):

  for j in range(rows-i):
    print(" ",end=" ")

  for k in range(2 * i - 1):
    print("*", end= " ")
  print()    

  
