#lambda function - lambda n : n * n
#Square of given numbers
sq = lambda n:n*n
print("The square of 5 is: ",sq(5)) 
print("The square of 4 is: ",sq(4)) 

#sum of 2 given numbers
s = lambda a,b : a +b
print("The sum of 10,20 is: ",s(10,20))
print("The sum of 100,200 is: ",s(100,200))

#check even
is_even = lambda n:n%2==0
print(is_even(5))

#print maximum number
max_num = lambda a,b : a if a>b else b
print("Maximum number is: ",max_num(10,20))

#filter()func -  we can use filter function to filter values from given sequence based on some conditions
li = [1,2,3,4,5,6,7,8,9,10]
even_list = list(filter(lambda x:x%2==0,li))
odd_list = list(filter(lambda x:x%2!=0,li))
print("Even numbers: ",even_list)
print("Odd numbers: ",odd_list)

names = ["jonas","jason","tharun","srikanth"]
result = list(filter(lambda name:name.startswith("j"),names))
print(result)

#filter() func - without lambda
def is_even(x):
  if x%2==0:
    return True
  else:
    return False
li = [1,2,3,4,5,6,7,8,9,10]
l1 = list(filter(is_even,li))
print(l1)


#map() function - perform double and generate new list of doubles
#squres each numbers
l1 = [1,2,3,4,5]
double = list(map(lambda x:x*x,l1))
print(double)

#length of each string
words = ["jason","jonas","Tharun","srikanth"]
result = list(map(lambda w:len(w),words))
print(result)

#map() func - without lambda
l1 = [5,4,3,2,1]
def double(x):
  return x*x
res = list(map(double,l1))
print(res)

#reduce() func - reduces the sequence of elements into a single element
from functools import *
li = [10,20,30,40,50]
res = reduce(lambda x,y:x+y,li) 
result = reduce(lambda x,y:x*y,li) 
print(res)
print(result)

#sorted
li = [(1,5), (2,3), (4,1)]
sorted_li = sorted(li,key = lambda x:x[1])
print(sorted_li)

fruits = ["apples","banana","kiwi","grapes"]
sort = sorted(fruits, key = lambda x:len(x))
print(sort)

li = ["Cat", "Apple", "Banana", "Dog"]
sortedli = sorted(li, key = lambda x:x.lower())
print(sortedli)

