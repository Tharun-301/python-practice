lst = [5,4,3,3,4,5]
# rev = lst[::-1]
rev = list(reversed(lst))
if rev == lst:
  print('Palindrome')
else:
  print('Not Palindrome')  

