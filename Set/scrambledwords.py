#anagram words
word_set = {'plea', 'medical', 'listen', 'leap', 'decimal'
    , 'silent', 'pale', 'enlist'}

result = set()

for i in word_set:
  for j in word_set:
    if i != j and sorted(i)==sorted(j):
      pair = tuple(sorted((i,j)))
      result.add(pair)

for pair in  result:
  print(pair)  
