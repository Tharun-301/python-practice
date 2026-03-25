n = int(input('Enter the number: '))
x = n 
sum = 0
while x>0:
  r = x%10
  sum += r
  x = x//10
if n%sum == 0:
  print(n,'is Harshad number')  
else:
  print(n,'not a Harshad number')  