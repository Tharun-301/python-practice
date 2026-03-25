FILENAME = 'journal.txt'

def write_entry():
    entry = input('Write your journal entry: ') + '\n'
    with open(FILENAME,'a', encoding='utf-8') as f:
        f.write(entry)

def read_all():
    with open(FILENAME,'r', encoding='utf-8') as f:
        print('\n All Journal Entries')
        print(f.read())

def search():
    keyword = input('Enter keyword to search: ')
    with open(FILENAME,'r', encoding='utf-8') as f:
        all_lines = f.readlines()
        for line in all_lines:
            if keyword.lower() in line.lower():
                print(line.strip())
                return
    print('No matching found')


def main_menu():
    while True:
        print("---------File Journal Manager----------")
        print("1. Add Entry")
        print("2. Read All Entries")
        print("3. Search Entries")
        print("4. Exit")

        choice = input('choose option from(1-4): ')

        if choice == '1':
            write_entry()
        elif choice == '2':
            read_all()
        elif choice == '3':
            search()
        elif choice == '4':
            print('Goodbye')
            break
        else:
            print('Invalid choice')

if __name__ == "__main__":
    main_menu()
