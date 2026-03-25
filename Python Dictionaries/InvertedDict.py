original = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3, 'f': 2}

inverted = { }

for key, value in original.items():
    if value not in inverted:
        inverted[value] = {key}
    else:
        inverted[value].add(key)    

print("Inverted Dictionary = ",inverted)
