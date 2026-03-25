#Capitalize First Letter of Each Word
s = "python string interview questions"
res = ""
make_upper = True
for ch in s:
    if make_upper and ch != " ":
        if 'a' <= ch <= 'z':
            res += chr(ord(ch) - 32)
        else:
            res += ch
        make_upper = False
    else:
        res += ch
    if ch == " ":
        make_upper = True
print(res)