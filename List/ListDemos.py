#list
l1 = [1,2,3,4,5]
l2 = [1.2,1.2,2.3,5.1,6.2]
l3 = ['jason','Tharun','jonas']
print(l1)
print(l2)
print(l3)

# creation
l1 = list((2,3,4,5))
l2 = list('abcd')
print(l1,l2)

#creating a list with heterogeneous elements
a = 8
list = [3,'four',a,2.1]
print(type(list))
print(list)

#creating a list of list
a = 4
list1 = [3,'four',a, 2.1,True]
list2 = [1,2,list1]
print(list2)

#length of a string
a = 4
list1 = [3,'four',a,2.1,True]
print(len(list1))

#we can give indexing values +pos and -neg
b = 3
list = [2,'apple',4.3,b]
print(list[2])
print(list[-3])

#iterating over a list# membership also in, not in
a = False
list = [2,'apple',4.3,a]
for item in list:
  print(item)

# #List Concatenation
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d"]
list = list1+list2
print(list)

#adding items to the list
list = []
for i in range(1,5):
  list += [i]
print(list)

#adding element to the list
list = [1,2,3,4]
list.append(5)
print(list)

#Repition
list = [1,2,3,4,5]
li = list*3
print(li)