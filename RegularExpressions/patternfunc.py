# import re
# print(re.match('abc','abcde'))
# print(re.fullmatch('python','python').group())
# print(re.search('very','python is very easy'))#.span()
# print(re.findall('can','can you can a can as a canner'))

mydate = input('Enter the date in day/month/year: ')
li = mydate.split('/')
print('day',li[0])
print('month',li[1])
print('year',li[2])