def count_case(word):

  upper = 0
  lower = 0
  
  for ch in word:
    ascii = ord(ch)

    if ascii >= 65 and ascii <= 90:
      upper += 1
    elif ascii >= 97 and ascii <= 122:
      lower += 1
  return upper, lower       

word = input('Enter the word: ')
upper_count, lower_count  = count_case(word)

print("Upper count =",upper_count)
print("Lower count =",lower_count)