s = 'success'
done = ''
for ch in s:
  already = False
  for d in done:
    if d == ch:
      already = True
      break
  if not already:
    count = 0
    for c in s:
      if c==ch:
        count +=1  
    print(ch, '=',count)  
    done += ch  


