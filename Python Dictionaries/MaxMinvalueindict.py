#Find maximum value and its key
d = {'a': 5, 'b': 9, 'c': 2}
max_value = float('-inf')
#max_value = -999999

max_key = " "
for k in d:
 if d[k]>max_value:
  max_value = d[k]
  max_key = k
  
print(max_key,'=',max_value)  


#Find minimum value and its key
d = {'a': 5, 'b': 9, 'c': 2} 
min_value = 999999
min_key = " "

for k in d:
  if d[k] < min_value:
   min_value = d[k]
   min_key = k

print(min_key,"=",min_value)   
