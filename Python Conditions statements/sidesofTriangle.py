side1 = float(input("Enter the length of  side1: "))
side2 = float(input("Enter the length of side2: "))
side3 = float(input("Enter the length of side3: "))

if side1+side2 > side3 and side1+side3 > side2 and side2+side3 > side1:
  print("Three sides forms a triangle")
else:
  print("These three cannot form a triangle")  