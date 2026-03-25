# Read - error if it doesn't exist

f = open("filedata.txt")
# print(f.read())
# print(f.read(4))# we can give size to read(5)

# print(f.readline())#it reads only one line from the data
# print(f.readlines())#it we can read entire lines returns list

for line in f:
    print(line)

f.close()

# # with - Automatically closes the file.
# with open("filedata.txt",'r') as f:
#     data=f.read()
#     print(data)
# print(f.closed)

try:
    f = open("filedata.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

FILENAME = input('todolist.txt')

def write_entry():
  entry = input('Enter your to-dolist entry: ')
  with open(FILENAME,'a',encoding='utf-8') as f:
    print(f.write(entry))
    print("added successfully.\n")

def read_all():
    with open(FILENAME, 'r', encoding='utf-8') as f:           
        print('\n All To-Do list Entries')
        print(f.read())

def search_entries():
  keyword = input('Enter keyword to search: ')
  with open(FILENAME,'r',encoding='utf-8') as f:
    all_lines = f.readlines()
    for line in all_lines:
      if keyword.lower() in line.lower():
                print("Found:", line.strip())
                return
  print("No matching task found.\n")

def delete_entry():
    to_delete = input('Enter entry to delete: ')
    with open(FILENAME, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(FILENAME, 'w', encoding='utf-8') as f:
        found = False
        for line in lines:
            if to_delete.lower() == line.strip().lower():
                found = True
                continue
            f.write(line)

    if found:
        print(" deleted successfully.\n")
    else:
        print("Task not found.\n")


def main_list():
  while True:
    print("------ To-Do List File Manager ------")

    print("1. Add Entry")
    print("2. Read All Entries")
    print("3. Search Entries")
    print("4. Delete Entries")
    print("5. Exit")

    choice = input('choose option from(1-5): ') 

    if choice == '1':
      write_entry()
    elif choice == '2':
      read_all()
    elif choice == '3':
      search_entries()
    elif choice == '4':
      delete_entry()
    elif choice == '5':
      print('GoodBye')
      break
    else:
      print('Invalid option')        

if __name__ == "__main__":      
  main_list()      