with open('data.txt','r') as f:
  ch1 = f.read(1)
  print(ch1)
  ch2 = f.read(3)
  print(ch2)
  ch3 = f.read()
  print(ch3)
