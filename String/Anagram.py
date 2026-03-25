str1 = input('Enter the phrase1: ')
str2 = input('Enter the phrase2: ')
str1 = str1.lower()
str2 = str2.lower()
for ch in str1:
  if ch.isalpha():
    if str1.count(ch)==str2.count(ch):
      print(' Anagram')
      break
else:
  print('Not Anagram')      
