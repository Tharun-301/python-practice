a = 12
b = 18

#find GCD first
x = a
y = b

while y>0:
  x, y = y, x % y

  gcd = x

  lcm = (a*b) // gcd
print("LCM is:",lcm) 

