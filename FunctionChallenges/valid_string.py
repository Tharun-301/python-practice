def valid_string(string):
  
    valid_len = len(string) >= 6
    first_ch = string[0].isdigit()
    
    if valid_len or first_ch:
        res = 'Valid String'
    else:
        res = 'Invalid String'
    return res

string =  input('Enter the word: ')
result = valid_string(string)
print(result)
