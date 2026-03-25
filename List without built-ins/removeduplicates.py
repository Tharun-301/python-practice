list = [1,2,2,3,4,4,1]
unique = []

for x in list:
  exist = False
  for y in unique:
    if x == y:
      exist = True
      break
  if not exist:
    unique += [x]  
    
print(unique)    