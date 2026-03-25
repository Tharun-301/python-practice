#Divisible by numbers
def divisible(arg):

    remainder = arg % 3
    if remainder == 0:
        Result = True
    else:
        Result = False
    print(Result)   
     
n = int(input('Enter the number: '))     
divisible(n)        


#checking numbers
def is_between_200_and_500(number):

  if number >=200 and number <=500:
    print('Yes')
  else:
    print('No')  
number = int(input('Enter the number: '))
is_between_200_and_500(number)    


#Discount amount
def get_discount(amount):
   
  if amount<500:
      print('Get 5% Discount')
  elif amount >= 500 and amount <= 2500:
     print('Get 10% Discount')
  else:
     print('Get 15% Discount')   

amount = int(input('Enter the amount: '))     
get_discount(amount)


#print numbers from 1 to n
def print_numbers(number):

  for num in range(1,number+1):
    print(num)

number = int(input('Enter the number: '))
print_numbers(number)


#Print Even Odd with in     dex numbers
def shows_numbers(number):
  
  for i in range(number+1):
    if i%2==0:
      print(str(i) + " Even")
    else:
      print(str(i) + " Odd")

number = int(input('Enter the number: '))
shows_numbers(number)