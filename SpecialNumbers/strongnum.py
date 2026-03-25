n = int(input('Enter the number: '))
temp = n
sum = 0
while temp>0:
  digit = temp%10
  fact = 1
  for i in range(1,digit+1):
    fact = fact * i
  sum += fact
  temp = temp//10
if n == sum:
  print(n,'is strong number')
else:
  print(n,'is not strong number')       