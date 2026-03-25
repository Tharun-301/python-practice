tuple = (10,20,30,40)
i = 0
while i < 4:
  print(tuple[i])
  i += 1

#Find the length of a tuple (without len())
t = (5, 10, 15, 20, 25)

count = 0
for _ in t:
  count += 1
print('length -',count)  

#Access tuple elements using index
t = (11, 22, 33, 44, 55)
print("First:", t[0])
print("Last:", t[4])