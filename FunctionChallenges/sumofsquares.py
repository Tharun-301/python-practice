def sum_of_squares(m,n):

  total = 0
  for i in range(m,n+1):
    total += (i**2)
  return total

m = int(input('Enter the number1: ')) 
n = int(input('Enter the number2: ')) 
result = sum_of_squares(m,n)
print(result)
