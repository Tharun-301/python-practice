s = '12345'
is_numeric = True
for ch in s:
  if ch<'0'or ch>'9':
    is_numeric = False
    break
print(is_numeric)  