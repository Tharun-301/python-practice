#Angaram
s1 = input('Enter the string1: ')
s2 = input('Enter the string2: ')

if len(s1)!=len(s2):
  print('Not Anagram')
else:
  is_anagram = True
  for ch in s1:
    c1 = 0
    c2 = 0

    for x in s1:
      if x==ch:
        c1+=1

    for y in s2:
      if y==ch:
        c2+=1

    if c1 != c2:
      is_anagram = False
      break
if is_anagram:
  print('Anagram')      
else:
  print('Not Anagram')    