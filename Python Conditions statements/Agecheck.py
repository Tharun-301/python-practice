#check age for work
# age = int(input('Enter a number: '))
# if age>=18 and age<=60:
#   print('Eligible to work')
# else:
#   print('Not Eligible to work')  

# check for eligible to work from three people
age1 = int(input("Enter the person1 age: "))
age2 = int(input("Enter the person2 age: "))
age3 = int(input("Enter the person3 age: "))

legal_age = 0

if age1 >= 18:
  legal_age +=1
if age2 >= 18:
  legal_age += 1
if age3>=18:
  legal_age +=1    

print(f"Out of three persons, {legal_age} persons are eligible to Work.")  