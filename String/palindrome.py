str = input('Enter the string: ')
str1 = str.replace(" ","")
rev= str1[::-1]
if str1.casefold()== rev.casefold():
  print(str,'to',str1,'it is palindrome')
else:
  palindrome =  str1.casefold()+rev.casefold()
  print(palindrome,'palindrome')



