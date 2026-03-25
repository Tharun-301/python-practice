n = int(input('Enter the number: '))
x = n
sqr = n*n
flag = 0
t = 10
while n>0:
  r = sqr%t
  if r==x:
    flag = 1
    break
  t *= 10
  n = n//10
if flag == 1:
  print(x,'is Automorphic number')
else:
  print(x,'is not Automorphic number')  