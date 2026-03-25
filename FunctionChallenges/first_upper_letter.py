#first upper letter from string

def get_first_upper_letter(string):
  for ch in string:
    if 'A' <= ch <= 'Z':
      return ch
  return -1  

string = input('Enter the string: ')
result = get_first_upper_letter(string)
print(result)

#If we want second upper letter from string
def get_second_upper_letter(string):
  count = 0
  for ch in string1:
    if 'A'<= ch <= 'Z':
      count +=1
      if count==2:
        return ch
  return -1
  

string1 = input('Enter the string: ')
result = get_second_upper_letter(string1) 
print(result)