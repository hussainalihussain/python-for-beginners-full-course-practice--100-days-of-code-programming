class Library:
  def __init__(self, books = []):
    self.books = books
    self.no_of_books = len(self.books)
  
  def add_book(self, book):
    if not book:
      return
  
    self.books.append(book)
    self.no_of_books = len(self.books)
  
  def display_length(self):
    print(f"No of books: {self.no_of_books}")

  def display_books(self):
    print("Display of books:")

    for book in self.books:
      print(f"* {book}")

library = Library([
  "Programming PHP",
  "Python Crash Course",
])

library.add_book("Automate the Boring Stuff with Python")
library.add_book("") # not allowing to enter empty (title) of book

library.display_length()
library.display_books()

library.add_book("Python Cookbook")

library.display_length()
library.display_books()