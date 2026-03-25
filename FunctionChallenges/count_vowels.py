def count_vowels(word):

  count = 0
  for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
      count += 1
    elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
      count += 1  
      
  return count

word = input('Enter the word: ') 
result = count_vowels(word)
print(result)   
