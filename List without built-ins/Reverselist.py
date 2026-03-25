list = [1,2,3,4,5]
rev = []

count = 0
for _ in list:
  count += 1

i = count -1

while i>=0:
  rev += [list[i]] 
  i -= 1

print(rev)  


