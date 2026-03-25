def calculate_percentage(number):
  if number < 1000:
    value = ((5/100)*500)
  else:
    value = ((10/500)*500)
  return value

number = int(input('Enter the number: '))    
result = calculate_percentage(number)
print(result)