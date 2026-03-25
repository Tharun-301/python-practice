# num1 = 1,2,3,4,5,6
# num2 = 2,4,5,9,10
# new_list = []
# n1 = set(num1)
# n2 = set(num2)
# common = n1 & n2
# print(sorted(common))


# Take input and split by comma
num1 = input("Enter first list: ").split(",")
num2 = input("Enter second list: ").split(",")

# Convert each element to int and make sets
n1 = set([int(i) for i in num1])
n2 = set([int(i) for i in num2])

# Find intersection
common = n1 & n2
print(sorted(common))
