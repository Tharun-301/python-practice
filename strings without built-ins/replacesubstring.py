s = "I like c, c++, and Java"
old = "Java"
new = "Python"

# Find length of string s manually
n = 0
for _ in s:
    n += 1

# Find length of old string manually  
m = 0
for _ in old:
    m += 1

res = ""  # Result string where we'll build the output
i = 0     # Index to traverse through the original string

# Loop through each character in the original string
while i < n:
    j = 0
    match = True
    
    # Check if there's enough characters left to match the old string
    if i + m <= n:
        # Compare each character of potential match
        while j < m:
            # Check if character at current position matches old string
            if s[i+j] != old[j]:
                match = False
                break
            j += 1
    else:
        match = False

    # If we found a complete match for the old string
    if match:
        res += new      # Add the new string to result
        i += m          # Skip over the old string we just replaced
    else:
        res += s[i]     # Add current character to result
        i += 1          # Move to next character

print(res)