# #Square pattern
# for i in range(1,6):
#   for j in range(1,6):
#     print('*', end=' ')
#   print()  

# #  Right Angled triangle
# for i in range(1,6):
#   for j in range(i):
#     print("*",end=' ')
#   print('')

# for i in range(1, 6):
#   for j in range(1, 6):
#     if i >= j :
#       print('*', end=' ')
#   print('')

# for i in range(1,6):
#   for j in range(1, i+1):
#     print('*', end=' ')
#   print('')    

# for i in range(1, 6):
#   print('* ' * i)  '''

# #left-aligned triangle
# for i in range(1, 6):
#   for j in range(1, 7-i):# 6-(i-1)
#     print('*', end = ' ')
#   print('')  

# for i in range(1,6):
#   print('* '*(6-i))

# #inverted right - Angled triangle
# for i in range(1, 6):
#   print(' '*(i-1), end = '')
#   print('*' * (6-i))

#inverted left-Aligned triangle
# for i in range(1,7):
#     print(' ' * (6-i), end = ' ')
#     print('*' * (i-1))

#square pattern
for i in range(1,6):
  for j in range(1, 6):
    print('*', end='')
  print('')

#rigth angled triangle
for i in range(1,6):
  for j in range(i):
    print('*', end='')
  print('') 
for i in range(1,6):
  for j in range(1,i+1):
    print('*',end = '')
  print('')
for i in range(1,6):
  print('*'*i)    
for i in range(1,6):
  for j in range(1,6):
    if i >= j:
      print('*',end='')
  print('')
#left aligned triangle
for i in range(1, 6):
  for j in range(1,7-i):
    print('*',end='')
  print()    

for i in range(1,6):
  print('*'*(6-i))

#inverted left angled triangle
for i in range(1,6):
  print(' '*(i-1),end='')
  print('*'*(6-i))
  
#right aligned left triangle
for i in range(1,6):
  print(' '*(5-i),end = '')
  print('*'*i)