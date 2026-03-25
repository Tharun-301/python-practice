#id
list1 = [1,2,3]
list2 = [1,2,3]
print(id(list1))
print(id(list2))

#modfying-list1
list_a = [1,2,3]
list_b = list_a
print(id(list_a))
print(id(list_b)) 

#the reason + str(...) is used is only because 
# Python doesn’t let you directly add (concatenate) a string and a list.

#modifying-list2
list_a = [1,2,3,4,5]
list_b = list_a
list_b[3] = 7
print('list_a: ', str(list_a))
print('list_b: ', str(list_b))

#modifying - list3
list_a = [1,2,3,4]
list_b = list_a
list_a = [1,2]
print('list_a: ',list_a)
print('list_b: ',list_b)

'''#list_b[3] = 4 modified the same list object (both names saw the change).
   #list_a = [1,2] created a new list and reassigned list_a to it (breaking the link with list_b).'''

#modifying - list4
list_a = [1,2,3]
list_b = list_a
list_a = list_a + [4,5]
print('List_a: ',list_a) 
print('list_b: ',list_b)

#modifying - list5
list_a = [1,2,3]
list_b = list_a
list_a += [4,5]
print('list_a :',list_a)
print('list_b :',list_b)

#modifying - list6
list_a = [2,3]
list_b = [1,list_a]
list_a[1] = 4
print(list_a)
print(list_b)

#modifying - list7
a = 8
list_a = [1,a]
print(list_a)
a = 2
print(list_a)

