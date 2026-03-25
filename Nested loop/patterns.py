# num = int(input('Enter a number: '))
# for row_num in range(0,num):
#   row_output = ""
#   seq_num = num - row_num
#   while seq_num > 0:
#     row_output = row_output + str(seq_num)
#     seq_num = seq_num -1
#   print(row_output)

num = int(input("Enter a number: "))
for row_num in range(1,num+1):
  row_output = " "
  seq_num = 1
  while seq_num <= row_num:
    row_output = row_output + str(seq_num)
    seq_num = seq_num + 1
  print(row_output)
  

