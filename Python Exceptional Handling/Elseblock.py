#try → code that may give error

#except → runs when error happens

#else → runs only when NO error happens 
# else = success message / success code

#Division
a= int(input('Enter the number: '))
b= int(input('Enter the number: '))
try:
   res = a//b
except ZeroDivisionError:
   print("Cannot divide by zero")   
else:
   print("Divided successfully: ",res) 


#List index
mylist = [10,20,30,40,50] 

try:
   value = mylist[9]
except IndexError as msg:
   print(msg)
else:
   print("Element found:", value)      
