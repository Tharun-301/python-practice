#Append
list = [1,2,3,4,5]
list.append(6)
print(list)
list[len(list):] = [8]
print(list)

li = []
li.append(10)
li.append('Python')
li.append([1,2,3])
print(li)

#Extend
list = [1,2,3]
list.extend([4])
print(list)
list.extend([5,6,7])
print(list)
list.extend('abc')
print(list)
list[3:7:] = [9,8]
print(list)
list[len(list): ] = [2,1]
print(list)


#copy
list1 =[5,6,7,8,9]
list2 = list1.copy()
print(id(list1)) 
print(id(list2))
print(list1)
print(list2)


#Removing elements
#pop- removes the last digit for default and index
list = [1,2,3,4,5]
list.pop()
print(list)

#remove - removes the mentioned element from list
list = [1,2,3,4,5]
list.remove(4)
print(list)

#clear -  removes all the elements
list = [1,2,3,4]
list.clear()
print(list)

#del -  it removes index, slicing and delete all the elements
list = [1,2,3,4,5]
del list[3]
print(list)
list1 = [1,2,3,4,5,6,7]
del list1[2:6]
print(list1)
list3 = [1,2,3,4]
del list
print(list3)