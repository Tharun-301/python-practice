L = [10,20,30,40,50]

try:
  try:
    index = int(input('Enter the index: '))
  except ValueError as e:
    print(e)  
  print(L[index])   
except IndexError as e:
  print(e)
  
except Exception as e:
  print(e)