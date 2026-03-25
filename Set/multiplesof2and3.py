n = int(input('Enter the number: '))
mul_2 = {i*2 for i in range(1,n+1)}
mul_3 = {i*3 for i in range(1,n+1)}

first_out = sorted(mul_2 - mul_3)

second_out = sorted((mul_2|mul_3)-(mul_2&mul_3))

print(first_out)
print(second_out)




