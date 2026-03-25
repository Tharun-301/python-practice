a = [5, 3, 2, 1, 6, 8, 9]
max1 = a[0]
max2 = -999999

for x in a:
  if x > max1:
    max2 = max1
    max1 = x
  elif x > max2 and x != max1 :
    max2 = x
print(max2)    