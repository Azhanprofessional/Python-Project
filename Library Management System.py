# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_barrowed = False

    def display_info(self):
        status = "Available" if not self.is_barrowed else "Barrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by '{author}' added to the library.")

    # view all books
    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Library Catalog ---")
            for book in self.books:
                book.display_info()

    # Borrow a book
    def barrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_barrowed:
                book.is_barrowed = True
                print(f"Book '{title}' has been borrowed. Enjoy Reading")
                return
        print(f"Book '{title}' is not available for barrowing.")

    # Return a book
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_barrowed:
                book.is_barrowed = False
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' is not in the library.")

# Main Program
library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add book")
    print("2. View books")
    print("3. Barrow book")
    print("4. Return book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        library.add_book(title, author)

    elif choice == '2':
        library.view_books()

    elif choice == '3':
        title = input("Enter book title to barrow: ").strip()
        library.barrow_book(title)

    elif choice == '4':
        title = input("Enter book title to return: ").strip()
        library.return_book(title)

    elif choice == '5':
        print("Exiting the library management system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")

