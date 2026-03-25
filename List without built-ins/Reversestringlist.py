#Reverse each string in the list
# word = ['abc','xyz']
# rev_list = []

# for w in word:
#   rev = ''
#   count = 0
#   for _ in w:
#     count += 1
#   i = count - 1
#   while i>=0:
#     rev += w[i]
#     i -= 1
#   rev_list += [rev] 
# print(rev_list)      

#Reverse the list & reverse each string
word = ['abc','xyz','hello']
rev_list = []

count = 0
for _ in word :
  count += 1

i = count - 1
while i>= 0:
  w = word[i]
  rev = ''

  length = 0
  for _ in w:
    length += 1

  j = length - 1
  while j>=0:
    rev += w[j]
    j -= 1

  rev_list += [rev]
  i -= 1

print(rev_list)     
