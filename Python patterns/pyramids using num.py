# half pyramid
rows = 5
for i in range(1,rows+1):
  for j in range(1, i+1):
    print(j, end=" ") 
  print() 

#Inverted half pyramid  
rows = 5
for i in range(rows, 0, -1):
  for j in range(1, i+1):
    print(j,end=" ")
  print()  

#full pyramids using numbers
print("----full pyramid using numbers----")
rows = 5
for i in range(1, rows+1):
  for j in range(rows - i):
    print(" ", end = " ")

  for k in range(i, 2 * i):
    print(k, end = " ")

  for k in range(2 * i - 2, i-1, -1):
    print(k, end = " " )    

  print()



# Print Pascal’s Triangle
# number = (previous number × (row - column)) ÷ (column + 1)