#sorted(iterable, /, *,key = None, reverse = False)
list1 = [1,12,7,-3,8]
print(sorted(list1))

list1 = [1,12,7,-3,8]
print(sorted(list1,reverse=True))

list1 = [1,12,7,-3,8]
print(sorted(list1,key=abs))


#reversed(sequence, /)
list1 = [1,12,7,-3,8]
rev = reversed(list1)
print(list(rev))


#slice(start = 0,stop,step=1)
list1 = [10,20,30,40,50,60,70]
s = slice(5)
print(list1[s])


#iter(iterable) and next(iterator)
list1 = [10,20,30]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))