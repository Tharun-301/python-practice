# a = 2
# tuple = (2,"six",a,3.4)
# print(tuple)
# print(type(tuple))

# #Tuple with a Single Item
# a = (2,) #we should give (,) after the number, because if we won't give (,) it take as int type 
# print(type(a))
# print(a)

# #Accessing Tuple elements is also similar to string and list accessing and slicing.
# a = 3
# tuple = (2,"six",a,3.5)
# print(tuple[1])

#Tuples does not support modification.
tuple_a = (2,"six",4,5.6,7,9)
tuple_a[3] = 1
print(tuple_a)

# #String to Tuple
# color = "Red"
# tuple_b = tuple(color)
# print(tuple_b)

# #List to Tuple
# list = [1,2,3,4,5]
# tuple_a = tuple(list)
# print(tuple_a)

# #Sequence to Tuple
# tuple_a = tuple(range(5))
# print(tuple_a)

# #Membership Check - in, not in
# tuple_a = (1,2,3,4)
# is_part = 5 in tuple_a
# print(is_part) 

# tuple_a = (1,2,3,4,5)
# is_part = 1 not in tuple_a
# print(is_part)

# #List Membership
# list_a = [1,2,3,4,5]
# is_part = 1 in list_a
# print(is_part)

# #String membership
# word = "Python"
# is_part = "th" in word
# print(is_part)

# #Unpacking
# tuple_a = ('R', 'e', 'd')
# (s1,s2,s3) = tuple_a
# print(s1)
# print(s2)
# print(s3)

# tuple_a = ('R', 'e', 'd')
# s_1, s_2 = tuple_a
# print(s_1)
# print(s_2)

# tuple_a = ('R', 'e', 'd')
# s_1, s_2, s_3, s_4 = tuple_a
# print(s_1,s_2,s_3,s_4)

# #Packing
# tuple_a = 1,2,3,4
# print(tuple_a)
# print(type(tuple_a))

# tuple_a = "r","e","d"
# print(tuple_a)
# print(type(tuple_a))

# tuple_a = 1, #"a",
# print(tuple_a)
# print(type(tuple_a))

# tuple_a = 'R', 'e', 'd'
# s_1, s_2, s_3 = tuple_a
# print(s_1,s_2,s_3,)




