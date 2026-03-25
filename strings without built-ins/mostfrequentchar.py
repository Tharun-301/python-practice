s = 'barrow'
max_count = 0
max_char = ''
for ch in s:
  count = 0
  for c in s:
    if c == ch:
      count += 1
  if count > max_count:
    max_count = count
    max_char = ch
print(max_char,'-',max_count)   




