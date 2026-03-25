#index
list = [10,20,30,40,10,20,30,20,70]
print(list.index(20))
print(list.index(20,3))
print(list.index(20,6,8))

#count
print(list.count(20))

#reverse
list1 = [10,20,30,40,50,60,70]
list1.reverse()
print(list1)

#sort
list2 = [30,20,70,10,40,50,60]
list2.sort()
print(list2)

#list2.sort(reverse=False)#default
lis = [30,20,70,10,40,50,60]
lis.sort(reverse = True)
print(lis)




list3 = ['coat','bat', 'apple', 'python','cat']
list3.sort() 
print(list3)
list3.sort(key = len)
print(list3)

list4 = ['apple','Banana','cat','Dog']
list4.sort()#because of ascii codes it takes first upper case and then lower case
print(list4)
list4.sort(key = str.lower)
print(list4)