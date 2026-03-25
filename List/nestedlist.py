#We use nested in matrices
list = [1,2,3,[4,5],[6,7,8]]
print(list)
print(list[1])
print(list[3][1])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 3, 4],
    [2, 5, 6, 7]
]
# for i in range(4): #row index
#   for j in range(4): #column index
#     print(matrix[i][j], end=" ")
#   print( ) 

print(matrix[3][2])

data = [
    ["Item",    "Type",       "Price"],
    ["Apple",   "Fruit",      50],
    ["Carrot",  "Vegetable",  30],
    ["Milk",    "Dairy",      40],
    ["Rice",    "Grain",      60]
]

for row in data:
  print(f"{row[0]:<10} {row[1]:<12} {row[2]:>3}")