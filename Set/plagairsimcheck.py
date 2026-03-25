import re
str1 = ('Time is the most valuable thing we have,'
        ' and once lost, it never returns.')

str2 = ("We never get time back once it's "
    "gone—it's truly the most valuable resource.")

word1 = re.findall('\w+', str1.lower())
word2 = re.findall('\w+', str2.lower())

wset1 = set(word1)
wset2 = set(word2)

comman = wset1 & wset2
unique = wset1 | wset2

ratio = len(comman)/len(unique)
print(f'jaccard similarity:{ratio:.2f}')

