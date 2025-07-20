from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models

# Create the database tables (Normally use Alembic in real apps)
models.Base.metadata.create_all(bind=engine)

api = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Insert initial books on startup if DB is empty
@api.on_event("startup")
def startup_populate_db():
    db = SessionLocal()
    if db.query(models.Books).count() == 0:
        books = [
            {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-help", "year": 2018},
            {"title": "Deep Work", "author": "Cal Newport", "genre": "Productivity", "year": 2016},
            {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction", "year": 1988},
            {"title": "Clean Code", "author": "Robert C. Martin", "genre": "Programming", "year": 2008}, 
            {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History", "year": 2011}
        ]
        for book in books:
            db.add(models.Books(**book))
        db.commit()

# ✅ GET: View all books in plain text
@api.get('/books', response_class=PlainTextResponse)
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(models.Books).all()
    if not books:
        return "No books in the library."
    result = ""
    for book in books:
        result += f"{book.title} is a {book.genre} book written by {book.author} and published in {book.year}\n"
    return result

# ✅ GET: View single book by title
@api.get('/books/{title}', response_class=PlainTextResponse)
def get_book_by_title(title: str, db: Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.title == title).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"No book with title '{title}' found.")
    return f"{book.title} is a {book.genre} book written by {book.author} and published in {book.year}"

# ✅ POST: Add a new book
@api.post('/books')
def add_book(book: dict, db: Session = Depends(get_db)):
    db_book = models.Books(**book)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": "Book added successfully", "book": book}

# ✅ PUT: Update existing book
@api.put('/books/{title}')
def update_book(title: str, updated_book: dict, db: Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.title == title).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book '{title}' not found.")
    
    book.title = updated_book["title"]
    book.author = updated_book["author"]
    book.genre = updated_book["genre"]
    book.year = updated_book["year"]
    
    db.commit()
    return {"message": "Book updated successfully", "book": updated_book}

# ✅ DELETE: Delete a book by title
@api.delete('/books/{title}')
def delete_book(title: str, db: Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.title == title).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book '{title}' not found.")
    
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully", "title": title}
