n = int(input('Enter the number: '))
x = n+1
flag = 0 #found = False
for i in range(1,x):
  if i*i == x:
    flag = 1 #found = True
    break
if flag == 1 :
  print(n,'is sunny number') 
else:
  print(n,'is not sunny number')  

  
