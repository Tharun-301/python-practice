with open('data.txt','rb') as f:
  print(f.read(4))
  print(f.tell())
  #forward direction
  # print(f.seek(3,0))
  # print(f.read(2))
  # print(f.seek(3,1))
  # print(f.tell())
  # print(f.read(2))
  # backward direction
  # print(f.seek(-3,1))
  # print(f.read(2))
  print(f.seek(-4,2))
  print(f.read(2))