i = 10
s = 'Hello'
with open('data.txt','w') as f :
  print(f.write(str(i)))
  print(f.write(s))