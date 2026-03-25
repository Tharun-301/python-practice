def max(a,b,c,/):

  if a > b and a > c:
    return a
  elif b > c:
    return b
  else:
    return c
  
res = max(8,5,6) 
print(res) 