# Challenge Day 24

# Create a dataclass to represent a library book with fields for title, author, ISBN, and publication year, including a method to display book details

from dataclasses import dataclass

# ✅ Dataclass to represent a library book
@dataclass
class Library:
    title: str
    author: str
    isbn: str
    publication_year: str

    # 🔁 Class variable to store all book objects
    all_books = []

    # 🚀 Automatically called after object creation
    def __post_init__(self):
        # Add the current book object to the shared list
        Library.all_books.append(self)

    # 📄 Method to display book details
    def show(self):
        print(f"📘 Title: {self.title} | ✍️ Author: {self.author} | 🆔 ISBN: {self.isbn} | 📅 Year: {self.publication_year}")

# 🚪 Main function to run the program
def main():
    # Ask the user how many books they want to add
    n = int(input("How many books you want to add: "))

    # 📥 Take input for each book and create Library objects
    for _ in range(n):
        title = input("Enter the Book title: ")
        author = input("Enter the Book author: ")
        isbn = input("Enter the Book isbn: ")
        publication_year = input("Enter the Book publication year: ")
        Library(title, author, isbn, publication_year)  # Object auto-added to all_books

    # 📋 Display all stored books
    print("\n📖 List of All Books:\n")
    for i, book in enumerate(Library.all_books, 1):
        print(f'{i}. ', end="")
        book.show()

# ✅ Entry point of the program
if __name__ == "__main__":
    main()
