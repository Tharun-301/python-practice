list = [1,2,1,3,2,1]

done = []

n = 0
for _ in list:
  n += 1

for i in range(n):
  x = list[i]

  found = False
  for y in done:
    if x == y:
      found = True
      break
  if not found :
    count = 0
    for j in range(n):
      if list[j] == x:
        count += 1

    print(x,'-',count)      

    new_done = []
    for d in done:
      new_done += [d]
    new_done += [x]
    done += new_done  