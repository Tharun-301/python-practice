num_a = int(input('Enter the number: '))
num_b = int(input('Enter the number: '))

result = (num_a > 300 or num_b>0) and (num_a + num_b<500)
if result:
  print('We can team up')
else:
  print('We cannot team up')  