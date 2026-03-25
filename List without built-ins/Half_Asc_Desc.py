list = [4,8,9,5,1,2,7,6,3,10]

n = 0 
for _ in list:
  n += 1

for i in range(n):
  for j in range (i+1,n):
    if list[i]> list[j]:
        asc = list[i]
        list[i]= list[j]
        list[j] = asc

half = n//2
i = half
j = n-1

while i<j:
    desc = list[i]
    list[i] = list[j]
    list[j] = desc

    i += 1
    j -= 1

print(list)      
