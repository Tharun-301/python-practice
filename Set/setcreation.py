#set - is collection of elements and unoredered

#creation
a = 3
s1 = {1,2.3,"hi",a}
print(s1)
print(type(s1))

#Duplicate
s1 = {"a","b","c","a"}
print(s1)
print(type(s1))

'''#Immutable items- TypeError: unhashable type: 'list'
s1 = {1,2,3,[4,5]}
print(s1)
print(type(s1))'''

#Creating Empty Set
set_a = set()
print(type(set_a))
print(set_a)

#Converting to Set-set(sequence) takes any sequence as argument and converts to set, avoiding duplicates   
#List to Set
set_a = set([1,2,1])
print(set_a)
print(type(set_a))

#String to Set
set_a = set("Blue")
print(type(set_a))
print(set_a)

#Tuple to Set
set_a = set((1,2,1,3))
print(set_a)

'''#As sets are unordered, we cannot access or change an item of a set using Index and Slicing
set_a = {1,2,3,4}
print(set_a[3])
print(set_a[1:3]) #TypeError: 'set' object is not subscriptable'''

#set.add(value) adds the item to the set, if the item is not present already.
set_a = {1,2,3,4}
set_a.add(5)
print(set_a)

set_b = {10,20,30,40,50}#using hashtable  we can know order of values 
print(set_b) #h(x) = x%16 if keys reaches 8 changes then hash will be 64.
              
#set.update(sequence) adds multiple items to the set, and duplicates are avoided.
set_a = {1,2,3}
set_a.update([4,5,3])
print(set_a)

#set.discard(value) takes a single value and removes if present. if value is not there it will print sequence only, no error.
set_a = {1,2,3}
set_a.discard(4)
print(set_a)

#set_a.remove(value) takes a value and remove if it present it's print values, if not raise an error.
set_a = {1,2,3}
set_a.remove(9)
print(set_a)