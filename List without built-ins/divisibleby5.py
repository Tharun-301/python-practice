n = int(input('Enter a number: '))
list = []
for i in range(1,n+1):
  num = int(input('Enter the number: '))
  if num%5==0:
    list.append(num)
print(list)    
