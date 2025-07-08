# Challenge Day 26
# Develop a FastAPI application with endpoints to manage a 
# library of books, including creating, reading, updating, and deleting books


from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

api = FastAPI()

# 📚 Sample in-memory list of books (acts like a simple database)
all_books = [
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-help", "year": 2018},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Productivity", "year": 2016},
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction", "year": 1988},
    {"title": "Clean Code", "author": "Robert C. Martin", "genre": "Programming", "year": 2008}, 
    {"title": "Sapiens - A Brief History of Humankind", "author": "Yuval Noah Harari", "genre": "History", "year": 2011}
]

# ✅ GET: View all books in plain text format
@api.get('/books', response_class=PlainTextResponse)
def get_all_books():
    result = ""
    for book in all_books:
        result += f"{book['title']} is a {book['genre']} book written by {book['author']} and published in {book['year']}\n"
    return result

# ✅ GET: Read details of a single book by title
@api.get('/books/{title}', response_class=PlainTextResponse)
def get_book_by_title(title: str):
    for book in all_books:
        if book['title'] == title:
            return f"{book['title']} is a {book['genre']} book written by {book['author']} and published in {book['year']}"
    return f"No book with title '{title}' found in the library."

# ✅ POST: Add a new book to the list
@api.post('/books')
def add_book(book: dict):
    new_book = {
        "title": book['title'],
        "author": book['author'],
        "genre": book['genre'],
        "year": int(book['year'])
    }
    all_books.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

# ✅ PUT: Update a book’s details by title
@api.put('/books/{title}')
def update_book(title: str, updated_book: dict):
    for book in all_books:
        if book['title'] == title:
            book['title'] = updated_book['title']
            book['author'] = updated_book['author']
            book['genre'] = updated_book['genre']
            book['year'] = int(updated_book['year'])
            return {"message": "Book updated successfully", "book": book}
    return {"error": f"'{title}' not found in the library."}

# ✅ DELETE: Remove a book from the list by title
@api.delete('/books/{title}')
def delete_book(title: str):
    for index, book in enumerate(all_books):
        if book['title'] == title:
            deleted_book = all_books.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}
    return {"error": f"'{title}' not found in the library."}
