'''s = 'programming'
result = ''
for ch in s:
  if ch not in result: # <-- using built-in membership check 
    result +=ch
print(result)  '''  

s = 'programming'
result = ''
for ch in s:
  #flag acts as a signal to remember whether a character is already found in res.
  flag = True

  for r in result:
    if r == ch:
      flag = False
      break
    
  if flag:
    result += ch
print(result)      