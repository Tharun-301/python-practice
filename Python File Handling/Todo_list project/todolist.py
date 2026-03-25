FILENAME = 'todolist.txt'

def write_entry():
    entry = input('Enter your to-dolist entry: ') + '\n'
    with open(FILENAME,'a',encoding='utf-8') as f:
        f.write(entry)
        print("Added successfully.\n")

def read_all():
    with open(FILENAME, 'r', encoding='utf-8') as f:           
        print('\n--- All To-Do List Entries ---')
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
        print("Deleted successfully.\n")
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

        choice = input('Choose option (1-5): ') 

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
