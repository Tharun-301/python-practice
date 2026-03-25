n = int(input('Enter the digits: '))
rev = 0
while n>0:
  r = n % 10
  rev = rev*10+r
  n = n//10
print('Reverse of a number: ',rev)  