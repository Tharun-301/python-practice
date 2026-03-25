#using for loop
list = [5,6,7,8,9,10]
for x in list:
  print(x)

#Using for loop with index (range+len)
list =  [5,6,7,8,9,10]
for i in range(len(list)):
  print(f"index {i}: {list[i]}")

#using while loop
list = [5,6,7,8,9,10]
i = 0
while i < len(list):
  print(list[i])
  i += 1 

#using enumerate
list = [5,6,7,8,9,10]
for index, value in enumerate(list):
  print(f"{index}: {value}")

#using list comphrension
list = [2,3,4,5,6]
squares = [x*x for x in list]
print(squares)

#using map function 
li = [9,8,7,6,5]
squares = list(map(lambda x:x**x,li))
print(squares)
