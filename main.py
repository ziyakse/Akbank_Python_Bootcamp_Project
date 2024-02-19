class Library:
    def __init__(self):
        self.file_p = "books.txt"
        self.file = open(self.file_p, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Book title: ")
        author = input("Book author: ")
        release_year = input("Release year: ")
        num_pages = input("Number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added.")

    def remove_book(self):
        title_to_remove = input("Please enter title of the book to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        new_lines = [line for line in lines if title_to_remove not in line]
        self.file.truncate(0)
        self.file.seek(0)
        self.file.write('\n'.join(new_lines))
        print(f"Book '{title_to_remove}' removed successfully.")

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("There is no like this number")

del lib
