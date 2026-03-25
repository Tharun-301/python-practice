str1  = 'ABcdEfGhiJ'
lower = ''
upper = ''
for x in str1:
  if x.islower():
    lower += x
  else:
    upper += x
print('lower:',lower)    
print('upper:',upper)
str2 = upper+lower
print(str2)
print('totallength:',len(str2))      