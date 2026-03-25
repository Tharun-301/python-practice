A = int(input("Enter the number: "))
B = int(input("Enter the number: "))

start = min(A, B)
end = max(A, B)

for num in range(start, end +1):
  print(num, end = " ")
print( )  

# if A <= B:
#   start = A
#   end = B
# else:
#   start = B
#   end = A

# for num in range(start, end+1):
#   print(num, end = " ")    
# print( )  

#if we want backward direction
# if A <= B:
#   for num in range(A, B+1):
#     print(num, end = " ")
# else:
#   for num in range(A, B,-1):
#     print(num, end = " ")    