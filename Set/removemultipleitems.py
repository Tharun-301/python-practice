#Remove multiple items..
set1 = {10,20,30,40,50,60,70,80,100}
n = input('Enter the numbers: ')
new_list = []
num = n.split()
for i in num:
  i = int(i)
  new_list +=[i]
set2 = set(new_list)
result = set1 - set2
print(sorted(result))
