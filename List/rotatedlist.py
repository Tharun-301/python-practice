# lst = [1,2,3,4,5,6]
# n = int(input('Enter the number: '))
# rotated = lst[n:] + lst[:n]
# print(rotated)

lst = [1,2,3,4,5,6]
n = int(input('Enter the number: '))

original_lst = lst[:]
rotated_lst = lst[:]
while True:
  rotated_lst = rotated_lst[n:] + rotated_lst[:n]
  print(rotated_lst)
  if rotated_lst == original_lst:
     break


