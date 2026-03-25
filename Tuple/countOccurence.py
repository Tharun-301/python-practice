t = (1,2,3,2,5,2,4)
count = 0
num = t[0]

for x in t:
  c = 0
  for y in t:
    if x == y:
      c += 1
  if c > count:
    count = c
    num = x

print(num,'-',count,'times')
 