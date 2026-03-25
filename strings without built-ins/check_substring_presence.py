s = 'python programming'
sub  = 'tin'
found = False
 
n = 0
for ch in s:
  n += 1

m = 0 
for ch in sub:
  m += 1

for pos in range(n-m+1):
  all_match = True
  for k in range(m):
      if s[pos+k]!=sub[k]:
        all_match = False
        break
  if all_match:
    found= True
print(found)        
