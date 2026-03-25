#sunny number
n = int(input('Enter the number: '))
x = n+1
found = False #flag = 0
for i in range(1,x):
  if i * i == x:
    found = True #flag = 1
    break
if found == True:
  print(n,'is sunny number')  
else:
  print(n,'Not sunny number')  

