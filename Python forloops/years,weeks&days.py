# days = [800,786]

# for num in days:
#     years = num // 365
#     weeks = num % 365 // 7
#     days = num % 365 % 7  
#     print(f"{num} days = {years} years, {weeks} weeks, {days} days")

rows = 5
for i in range(1,rows+1):
  print(" "* (rows-i+2)+'* '*i,end='')
  print("  "*(rows- i+2)+'* '*i)