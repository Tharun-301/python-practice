li = []
for x in range(10):
  li.append(x)
print(li)  

list = [x for x in range(10)]
print(list)
list1 = [x for x in range(1,5)]
print(list1)
list2 = [x**2 for x in range(1,5)]
print(list2) 
list3 = [x.lower() for x in 'pYtHOn']
print(list3)
list4 = [int(x) for x in '12345']
print(list4)
list5 = [x for x in 'ab2c3d*!e' if x.isalpha()]
print(list5)
list6 = [x for x in (10,11,12,13,14) if x%2==0]
print(list6)

list = [2**x for x in range(1,6)]#power
print(list)

words = ['Pawan Kalyan','Mahesh babu','Prabhas','Ntr']
list1 = [w[0] for w in words]
print(list1)

num1 = [10,20,30,40]
num2 = [30,40,50,60]
li = [i for i in num1 if i not in num2]
print(li)
lis = [i for i in num1 if i in num2]
print(lis)
num3 = [i for i in num1 if i not in num2] + [j  for j in num2 if j not in num1 ]#Symmetric
print(num3)

words = "The quick brown fox jumps over lazy dog".split()
print(words)
list = [[w.upper(),len(w)]for w in words]
print(list)

words1 = "The fast dark animal hops above the slow pup.".split()
print(words1)
list = [[w.lower(),len(w)]for w in words1]
print(list)

num = [4,8,3,5,10,7,2,9,13,6]

even = [x for x in num if x%2==0]
odd = [x for x in num if x%2!=0]
print('Even numbers:',even)
print('odd numbers:',odd)
