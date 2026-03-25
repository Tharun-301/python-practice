height = float(input("Enter the height: "))
weight = float(input("Enter the weight: "))

BMI = weight/(height**2)

if BMI<18.5:
  category ="Undeweight"
elif BMI<25:
  category = "Normal Weight"
elif BMI<30:
  category ="Overweight"
elif BMI<35:
  category ="Obese"  
else:
  category ="Several obese"  

print("Your BMI is: ",BMI) 
print("Category: ",category) 

