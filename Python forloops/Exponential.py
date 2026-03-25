base = int(input("Enter the base: "))
exponent = int(input("Enter the exponential: "))
result = 1
for _ in range(1,exponent+1):
  result *= base
print("The result of base",base,"and raised to the power of ",exponent,"is: ",result)  