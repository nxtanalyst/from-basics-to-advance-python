'''Scenario: OOP-Based Royal Library Management System

This code simulates a Royal Library System where books can be added, borrowed, and returned using object-oriented principles.

Each book (Book) holds individual metadata and availability status.

The Library class centrally manages a catalog of books.

Class methods (add_books, borrow_book, return_book) allow for library-wide operations on the book list.

The static method welcome_note() serves as a general utility message.

The describe() method provides book summaries for users.

This system is perfect for basic inventory and lending management in small educational tools, console-based simulations, or as a prototype for larger GUI-based library systems.'''

class Book:
    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def describe(self):
        status = "Available" if self.available else "Borrowed"
        print(f"📖 Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {status}")

    def mark_borrowed(self):
        self.available = False

    def mark_returned(self):
        self.available = True


class Library:
    books = []

    @classmethod
    def add_books(cls, book):
        cls.books.append(book)

    @classmethod
    def show_available_books(cls):
        for book in cls.books:
            if book.available:
                book.describe()

    @classmethod
    def borrow_book(cls, title):
        for book in cls.books:
            if book.title == title and book.available:
                book.mark_borrowed()
                print(f"✅ '{title}' has been borrowed.")
                return
        print(f"❌ '{title}' is not available for borrowing.")

    @classmethod
    def return_book(cls, title):
        for book in cls.books:
            if book.title == title:
                book.mark_returned()
                print(f"🔁 '{title}' has been returned.")
                return
        print(f"❌ '{title}' not found in library.")

    @staticmethod
    def welcome_note():
        print("📚 Welcome to the Royal Library System! 📖")


# Create Book instances
b1 = Book("The Alchemist", "Paulo Coelho", "Fiction")
b2 = Book("A Brief History of Time", "Stephen Hawking", "Science")
b3 = Book("To Kill a Mockingbird", "Harper Lee", "Classic")

# Add books to the Library
Library.add_books(b1)
Library.add_books(b2)
Library.add_books(b3)

# Show welcome note
Library.welcome_note()

# Show all available books
print("\n--- 📘 Available Books ---")
Library.show_available_books()

# Borrow a book
print("\n--- 🛒 Borrowing Book ---")
Library.borrow_book("The Alchemist")

# Show available books after borrowing
print("\n--- 📉 Available Books After Borrowing ---")
Library.show_available_books()

# Return a book
print("\n--- 🔁 Returning Book ---")
Library.return_book("The Alchemist")

# Show available books after return
print("\n--- 📈 Available Books After Returning ---")
Library.show_available_books()

