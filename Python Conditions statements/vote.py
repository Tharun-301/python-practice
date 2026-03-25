n = int(input('Enter a number: '))
if n>=18:
  print('Eligible for Vote')
else:
  print('Not Eligible for vote')  



import datetime
year_of_birth = int(input("Enter the year of birth: "))

current_year = datetime.datetime.now().year

age = current_year - year_of_birth
 
if age >= 18:
  print(f"Person age is {age} and he is eligible for vote")
else:
  print("Person is not eligible for vote")  
