t = (1,2,3,4,5)

n = 4
found = False
for x in t:
  if x == n:
    found = True
    break
if found:
  print(found)
else:
  print('Not found')    
