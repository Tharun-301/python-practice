t = (10,20,30,40)
rev = ()

n = 0
for _ in t:
  n += 1

i = n-1

while i >= 0:
  rev += (t[i],)
  i -= 1

print(rev)  