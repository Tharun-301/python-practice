num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

if num1<=num2 and num1<=num3:
  if num2<=num3:
    print("The ascending numbers are in the order: ",num1, num2, num3)
  else:
    print("The ascending numbers are in the order: ",num1, num3, num2)
elif num2<=num1 and num2<=num3:
  if num1<=num3:
    print("The ascending numbers are in the order: ",num2, num1, num3)
  else:
    print("The ascending numbers are in the order: ",num2, num3, num1)
else:
  if num1 <= num2:
    print("The ascending numbers are in the order: ",num3, num1, num2)
  else:
    print("The ascending numbers are in the order: ", num3, num2, num1)              