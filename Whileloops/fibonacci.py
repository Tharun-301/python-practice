n = int(input("Enter the number: "))
previous_num = 0
current_num = 1
print("Fibonacci sequence upto: ",n)
while current_num <= n:
  print(previous_num)
  next_num = previous_num + current_num
  previous_num = current_num
  current_num = next_num