list = [10,20,40]
index = 2
value = 30
new = []

n = 0 
for _ in list:
  n += 1

i = 0
while i < n:  
  if i == index:
    new  =  new + [value]
  new = new + [list[i]]
  i += 1

print(new)    
