num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
n = int(input('Enter the number: '))

new_tuple = [t[:-1]+(n,) for t in num_list]

print(new_tuple)