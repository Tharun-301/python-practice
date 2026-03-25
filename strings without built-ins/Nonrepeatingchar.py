#first non repeating character
s = "aabbcdeff"

# find length manually
n = 0
for _ in s:
    n += 1

# print all non-repeating chars
for i in range(n):
    count = 0
    for j in range(n):
        if s[i] == s[j]:
            count += 1
    if count == 1:
        print(s[i])
