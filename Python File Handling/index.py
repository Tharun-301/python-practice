# file = open('sample.txt','r+')

# print(file.read())
# st = 'xyz'
# file.write(st)
# file.close()

#Cursor Position with tell()
with open('sample.txt','r') as f: 

  print(f.tell())     # cursor at start = 0

  f.read(5)           # read "Hello"
  print(f.tell())     # cursor moved to 5

  f.read(1)           # read space
  print(f.tell())     # cursor moved to 6

  f.close()

# Move Cursor with seek()
f = open('sample.txt','r')

f.seek(6)           # jump to position 6
print(f.read())     # read from 6 to end

f.close()

# Cursor after reading entire file
f = open('sample.txt','r')

content = f.read()

print(content)

print('cursor position: ',f.tell())

f.close()