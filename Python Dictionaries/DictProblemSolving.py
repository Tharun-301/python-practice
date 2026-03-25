#create a dict
d = {'a':1,'b':2,'c':3,'d':4}

for key in d:
  print(key ,':',d[key])

#count items in a dict
d = {'a':1,'b':2,'c':3,'d':4}

count = 0
for _ in d:
  count += 1
print('Total: ',count)


#Delete a specific key
d = {'a':1,'b':2,'c':3,'d':4}
key = 'd'
temp = { }

for k in d:
  if k != key:
    temp[k] = d[k]

d = temp
print(d)


#check if key is exist
d = {'a':1,'b':2,'c':3,'d':4}
key = 'b'
found = False
for k in d:
  if k == key:
    found = True
    break
print('Key found',found) 

#Get only the keys
d = {'a':1,'b':2,'c':3,'d':4}
key = []

for k in d:
  key += k

print(key)

##Get only the keys
d = {'a':1,'b':2,'c':3,'d':4}
values = []

for k in d:
  values += [d[k]]

print(values)  

#Merge two dictionaries manually
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = {}

for k in d1:
    merged[k] = d1[k]
for k in d2:
    merged[k] = d2[k]

print(merged)

#Sum of all dictionary values
d = {'a':11,'b':12,'c':13,'d':14}
sum = 0
for k in d:
  sum += d[k] 
print(sum)   

#Multiply all values
d = {'a':3,'b':4,'c':2,'d':5}
mul = 1
for k in d:
  mul *= d[k] 
print(mul)   
