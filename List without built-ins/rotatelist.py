list = [1,2,3,4,5]

n = 0
for _ in list:
  n += 1

last = list[n-1]

i = n-1

while i > 0:
  list[i] = list[i-1]
  i -= 1

list[0] = last  

print(list)

