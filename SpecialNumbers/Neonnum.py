n = int(input('Enter the number: '))
sqr = n*n
sum = 0
while sqr>0:
  digit = sqr%10
  sum += digit
  sqr = sqr//10
if n == sum:
  print(n,'is neon number')
else:
  print(n,'is not neon number')    
