# s = 'Python Programming'
# vowels = 'aeiouAEIOU'
# count = 0
# for ch in s :
#   if ch in vowels:
#     count +=1
# print(count)    

s = 'pyThOn ProGraMMing'
count = 0
for ch in s:
  # if (ch>='a'and ch<='z') or (ch>='A'and ch<='Z'):
    if ch >= 'A' and ch <= 'Z':   # If character is uppercase (A–Z in ASCII range 65–90)
      ch = chr(ord(ch) + 32)    # Convert uppercase to lowercase by adding 32 in ASCII

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch =='u':
      print(ch,end=' ')   
      count += 1   
print(', count:',count)        
