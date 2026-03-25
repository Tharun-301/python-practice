d = {'a': 1, 'b': 2, 'c': 3}
reverse_dict = { }

keys = [ ]
for k in d:
  keys[k] = [k]

n = 0
for _ in keys:
  n += 1

i = n-1
while i > 0 :
  k = keys[i]
  reverse_dict[k] += d[k]
  i -= 1

print(reverse_dict)   
