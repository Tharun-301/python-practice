import itertools
lst = [1,2,3]
# All permutations of length 3 (default is full length)
perms = list(itertools.permutations(lst))
print(perms)

#for length = 2
perms = list(itertools.permutations(lst,2))
print(perms)


import itertools as it

lst = ['A','B','C','D']
perms = it.permutations(lst,r=2)#r = len of permutations
perm_list = list(perms)
print('Permutations', perm_list)

for t in perm_list:
  print(t)

#combinations
from itertools import combinations

lst = [1, 2, 3]
combs = list(combinations(lst, 2))
print(combs)

'''#product
from itertools import product

a = [1, 2]
b = ['x', 'y']
prod = list(product(a, b))
print(prod)'''




