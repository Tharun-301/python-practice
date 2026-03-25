#SORT-Ascending
list = [5,3,1,6,2,4]

n = 0 
for _ in list:
  n += 1

for i in range(n):
  for j in range(i+1,n):
    if list[i] > list[j]:
      temp = list[i]
      list[i] = list[j]
      list[j] = temp

print('list Ascending order:',list)       


#SORT - Descending
list = [5,3,1,6,2,4]

n = 0
for _ in list:
  n += 1

for i in range(n):
  for j in range(i+1,n):
    if list[i]<list[j]:
      temp = list[i]
      list[i] = list[j]
      list[j] = temp

print('list Descending order:',list)
