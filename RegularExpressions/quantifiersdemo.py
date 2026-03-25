#quantifiers
# import re
# print(re.fullmatch('(ab)?','ab'))# ?- 0 or 1 
# print(re.fullmatch('(ab)?',''))
# print(re.fullmatch('(ab)*',''))# *- 0 or more
# print(re.fullmatch('(ab)*','abababababab'))
# print(re.findall('[abc]+','123 abcd basc bbacac@bca'))

#special characters
#Example1-firstname and lastname
# import re
# pattern_name= r"[A-Z][a-z]+ [A-Z][a-z]+"
# text1 = 'Abdul Bari'
# print(re.fullmatch(pattern_name,text1))

# #Example2-Variable name
# pattern_var = r"[a-zA-Z_][a-zA-Z0-9_]*"
# text2 = "item_1"
# print(re.fullmatch(pattern_var,text2))

# #Example- Time(HH:MM)
# pattern_time = r"[012][0-9]:[0-5][0-9]"
# text3 = "09:30"
# print(re.fullmatch(pattern_time,text3))

# #Example4 - DomainName 
# pattern_domain = r"[a-zA-Z0-9]+\.[a-z]+$"
# text4 = 'udemy.com'
# print(re.fullmatch(pattern_domain,text4))

#Escape sequences
import re

# \d - digit [0-9]
text = "My pin is 1234"
print(re.findall(r"\d+", text))  # ['1234']

# \D - non-digit
text = "Room42"
print(re.findall(r"\D+", text))  # ['Room']

# \w - alphanumeric [a-zA-Z0-9_]
text = "hello_world 123"
print(re.findall(r"\w+", text))  # ['hello_world', '123']

# \W - non-alphanumeric
text = "Price: $50"
print(re.findall(r"\W+", text))  # [': ', '$']

# \s - whitespace (space, tab, newline)
text = "Hello   World"
print(re.findall(r"\s+", text))  # ['   ']

# \S - non-whitespace
text = "   data123  "
print(re.findall(r"\S+", text))  # ['data123']

# \A - start of string
text = "Hello world"
print(re.findall(r"\AHello", text))  # ['Hello']

# \Z - end of string
text = "Hello world"
print(re.findall(r"world\Z", text))  # ['world']

