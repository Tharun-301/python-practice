def calculate_points(str):
  list = []
  num = 0
  for ch in str +',':
    if ch!=',':
      num = num * 10 + (ord(ch)-48)
    else:
      list.append(num)
      num = 0
  wins = list[0]
  draws = list[1]
  losses = list[2]

  total = wins * 4 + draws * 2 + losses * -1
  return total


str = input('Enter the string: ')  
result = calculate_points(str)
print(result)