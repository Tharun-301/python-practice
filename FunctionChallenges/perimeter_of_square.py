def perimeter_of_square(arg1):
   
  perimeter = arg1 * 4
  return perimeter

side = int(input('Enter the side: '))
result = perimeter_of_square(arg1=side)
print(result)