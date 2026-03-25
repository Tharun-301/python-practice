def fizz_buzz(number):
  if number%3==0 and number%5==0:
    res = "FizzBuzz"
  elif number%3 == 0:
    res = "Fizz"
  elif number%5 == 0  :
    res = "Buzz" 
  else:
    res = number
  return res

number  = int(input('Enter the number: '))
result = fizz_buzz(number)
print(result)
       