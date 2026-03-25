s = "He@ll#o! 123"
res = ''
for ch in s:
  if 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9' or ch == ' ':
    res += ch
print(res)    