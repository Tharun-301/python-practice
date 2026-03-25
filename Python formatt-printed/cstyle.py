'''#control characters
item = 'Memory'
size = 32
price = 11.5
print('cost of',size,'GB',item,'is $',price)#it taking spaces 
print('cost of %dGB %s is $%f'%(size,item,price))

name = 'Tharun'
roll_no = 12
avg = 73.6
print('student name is %s, and his rollno is %d, and avg %f'%(name,roll_no,avg))'''

'''#integer-control characters
data = 200
#print('%d'%(data))# it takes %decimal(mostly) and %integer for same values
print('%i'%(data))
print('%o'%(data))#octal by conversions
print('%x'%(data))'''

'''#float - control characters
data = 25.73009
print('%f'%(data))#float
print('%F'%(data))#Float
print('%g'%(data))#general float
print('%e'%(data))#scientiic
print('%E'%(data))#exponent'''

#string
data = 25
print('start %10d end'%(data))#we mention the distance with 10 
value = 25.132002
print('%2.3f'%value)# we can mention values of width from decimal