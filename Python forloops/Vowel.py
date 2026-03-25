sentence = input("Enter the sentence: ")

vowels_count = 0

for char in sentence:
  char_lower = char.lower()
  if char_lower in "aeiou":
    vowels_count += 1
print("Number of vowels",vowels_count)     
