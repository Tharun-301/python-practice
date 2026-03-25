def squares_list(str):

  list = []
  num = 0

  for ch in str + ',':  # add ',' to handle last number
    if ch!= ',':
      num = num * 10 + (ord(ch)-48)
    else:
      list = list + [num*num]  
      num = 0
  return list

str = input('Enter the numbers: ')  
result = squares_list(str)
print(result)  
