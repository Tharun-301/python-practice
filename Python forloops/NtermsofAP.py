a = int(input('Enter the intial term: '))
d = int(input('Enter the common difference: '))
n = int(input('Enter the number of terms: '))

for t in range(a,a+n*d,d):
  print(t)
