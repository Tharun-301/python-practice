import struct

File_Name = "library.dat"

FORMAT = 'i30s20si'
Record_size = struct.calcsize(FORMAT)


def pack_record(book_id, title, author, stock):
    title = title.encode().ljust(30)
    author = author.encode().ljust(20)
    return struct.pack(FORMAT, book_id, title, author, stock)


def unpack_record(record_bytes):
    book_id, title, author, stock = struct.unpack(FORMAT, record_bytes)
    return {
        "BookID": book_id,
        "Title": title.decode().strip(),
        "Author": author.decode().strip(),
        "Stock": stock
    }


def add_book():
    book_id = int(input("Enter the Book ID: "))
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    stock = int(input("Enter Stock: "))

    with open(File_Name, 'ab') as f:
        f.write(pack_record(book_id, title, author, stock))
    print("Book added successfully")


def view_book():
    print("\n====== Book Records ======")
    with open(File_Name, 'rb') as f:
        while True:
            record = f.read(Record_size)
            if not record:
                break
            book = unpack_record(record)
            if book["Stock"] > 0:    
                print(book)



def search_book():
    book_id = int(input("Enter Book ID to search: "))
    with open(File_Name, 'rb') as f:
        while True:
            record = f.read(Record_size)
            if not record:
                break
            book = unpack_record(record)
            if book["BookID"] == book_id:
                print("Book Found:", book)
                return
    print("Book not found")


def delete_book():
    book_id = int(input("Enter Book ID to delete: "))
    found = False

    with open(File_Name, 'rb+') as f:
        index = 0
        while True:
            f.seek(index * Record_size)
            record = f.read(Record_size)
            if not record:
                break

            book = unpack_record(record)

            if book["BookID"] == book_id:
                book["Stock"] = 0   # Logical deletion
                f.seek(index * Record_size)
                f.write(pack_record(
                    book["BookID"],
                    book["Title"],
                    book["Author"],
                    book["Stock"]
                ))
                print("Book deleted (Stock = 0)")
                found = True
                break

            index += 1

    if not found:
        print("Book not found")




from Book_manager import *

def show_menu():
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    show_menu()
