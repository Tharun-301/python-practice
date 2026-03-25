n = int(input('Enter the number: '))
sum = 0
for i in range(1,n):
  if n%i==0:
    sum += i
if n == sum:
  print(n,'is Perfect number')    
else:
  print(n,'is not perfect number')  