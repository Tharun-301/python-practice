def reverse_num(nums):
  rev = 0
  while nums>0:
    digit = nums%10
    rev = rev * 10 + digit
    nums = nums//10
  return rev
nums = int(input('Enter the digit: '))
res = reverse_num(nums)
print(res)

