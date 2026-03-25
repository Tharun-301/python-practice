s = "My name is python"

# Step 1: store letters only
letters = ""
for ch in s:
    if ch != " ":
        letters += ch

# Step 2: reverse letters manually
rev_letters = ""
i = len(letters) - 1
while i >= 0:
    rev_letters += letters[i]
    i -= 1

# Step 3: rebuild string keeping spaces
result = ""
i = 0

for ch in s:
    if ch == " ":
        result += " "
    else:
        result += rev_letters[i]
        i += 1

print(result)