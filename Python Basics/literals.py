#intliterals
a = 201
b = 123_456_789
print(a,b)

#floatliterals
c = 30.0
d = 3.15_77
e = 1.321e3
f = -2.345_23e-2
print(c,d,e,f)

#bool_literals
g = True
h = False
print(g,h)

#complexliterals
i = 2+4j
j = 1_2+1_6j
k = 2.4_6+5.7_8j
print(i,j,k)

#stringliterals
name = 'jason'
name1 = "jason"
name2 = '"jason"'
print(name,name1,name2)

#internationalformat
number = 123456789
print("{:,}".format(number))

#indianformat
def format_indian(number):
    num_str = str(number)[::-1]
    parts = []
    # First 3 digits
    parts.append(num_str[:3])
    num_str = num_str[3:]
    # Next groups of 2 digits
    while num_str:
        parts.append(num_str[:2])
        num_str = num_str[2:]
    return ','.join(parts)[::-1]

num = 123456789
print(format_indian(num))  # Output: 1,23,456,789