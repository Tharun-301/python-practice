#Tuple Comprehension
t1 = (x**2 for x in range(1,5))
# t1 = tuple(x**2 for x in range(1,5))
print(type(t1))

t2 = (*(x**2 for x in range(1,5)),)
print(t2)

t3 = (*(x.lower() for x in "pyTHOn"),)
print(t3)

'''t2 =tuple(x**2 for x in range(1,5))
print(t2)

t3 = tuple(x.lower() for x in "pyTHOn")
print(t3)'''

t4 =  (*(int(x) for x in "12345"),)
print(t4)

t5 = (*(x for x in 'abc*d7e' if x.isalpha()),)
print(t5)