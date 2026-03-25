# #clear()
# set_a = {1,2,3,4,5}
# set_a.clear()
# print(set_a)

# #length
# set_a = {1,2,3,4,5}
# print(len(set_a))

# #Iterating
# set_a = {1,2,3,4,5}
# for item in set_a:
#   print(item)

# #Membership check- not in, in
# set_a = {1,2,3,4,5}
# is_part = 11 not in set_a
# print(is_part)

# set_a = {1,2,3,4,5}
# is_part = 11 in set_a
# print(is_part)

# #set operations on mathematics
# #Union
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A.union(B)
# print(s1)

# ##we can use list sequence
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# li = [9,8,7]
# s1 = A.union(li)
# print(s1)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A|B
# print(s1)

# #Intersection
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A.intersection(B)
# print(s1)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A & B
# print(s1)

# #Intersection.update
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# A.intersection_update(B)
# print(A)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# A &= B
# print(A)

# #Difference
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A.difference(B)
# print(s1)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A-B
# print(s1)

# #Difference_Update
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# A.difference_update(B)
# print(A)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# A -= B
# print(A)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# B.difference_update(A)
# print(B)

# #Symmetric_difference
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A.symmetric_difference(B)
# print(s1)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# s1 = A^B
# print(s1)

# #Symmetric_difference-update
# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# A.symmetric_difference_update(B)
# print(A)

# A = {1,2,3,5,7}
# B = {5,7,9,10,11}
# A ^= B
# print(A)
