n = int(input('Enter the digits: '))
m = n
rev = 0
while n > 0:
  r = n % 10
  rev = rev * 10 + r
  n = n // 10
if rev == m:
  print('It is palindrome')
else:
  print('It is not palindrome')  





'''n = int(input('Enter the digits: '))
m = n
rev = 0
while n>0:
  r = n%10
  rev = rev*10+r
  n = n//10
if m == rev:
  print('It is palindrome')
else:
  print('It is not palindrome')  '''