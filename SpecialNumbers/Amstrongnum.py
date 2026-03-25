n = int(input('Enter the number: '))
x = n
y = n 
count = 0
while n>0:
  r = n%10
  count += 1
  n = n//10
sum = 0
while x>0:
  r = x%10 
  sum += r**count
  x = x//10
if y == sum:
  print(y,'is Amstrong number')  
else:
  print(y,'is not Amstrong number')  
