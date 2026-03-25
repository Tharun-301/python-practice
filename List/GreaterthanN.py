num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
n = int(input('Enter a number: '))
new_list = []
for i in num_list:
  if i>n:
    new_list += [i]
print(new_list)
   
