#list
L1 = [5, 6, 10, 11, 15]
it = iter(L1)          #iter() - give you items one by one
                       #next() - Gives the next element from that iterator.
print(next(it))  # 5 
print(next(it))  # 6
print(next(it))  # 10
print(next(it))  # 11
print(next(it))  # 15  If no more elements exist → Python raises StopIteration.

#Tuple
T1 = (5, 6, 10)
it = iter(T1)
print(next(it))  # 5

#Set
S1 = {7, 4, 9} # Sets have no order, so iterator may start anywhere.
it = iter(S1)
print(next(it))  # Could be 7 or 4 or 9 


#Dictionary
D1 = {'a': 1, 'b': 2}
it = iter(D1)
print(next(it))  # 'a'

#String
s = "Hello"
it = iter(s)
print(next(it))  # 'H'

#Range
r = range(3, 10)
it = iter(r)
print(next(it))  # 3