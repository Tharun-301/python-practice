import struct

record_size = 14

def add_player(id,name):
  with open('players.dat','ab') as file:
    name = name.encode().ljust(10)
    record = struct.pack('i10s',id,name) 
    file.write(record)

def find(index):
  with open('players.dat','rb') as f:
    f.seek(index * record_size)
    record = f.read(record_size)
    if record:
      id, name = struct.unpack('i10s',record)
      print(f"ID: {id}, NAME: {name.decode().strip()}")
    else:
      print("No record at the index")  

add_player(14, 'Naseer') 
add_player(16, 'Sanjay') 
add_player(1, 'Tharun') 
add_player(20, 'Vivek')   
add_player(4, 'Sai')    
find(2)