class InvalidAgeError(Exception):
  pass
def valid_age(age):
  if age >= 18 and age<= 60:
    return True
  else:
    raise InvalidAgeError("Age should be between 18-60")
   
name = input('Enter the name: ')
age = int(input('Enter the age: '))

try:
  valid_age(age)
  print("you can join work")
except InvalidAgeError as e:
  print(e)  
