class Library:
  def __init__(self, no_of_books, books):
    self.no_of_books = no_of_books
    self.books = books
  
  def all_books(self):
    print("All available books:")

    for book in self.books:
      print(f"* {book}")

  def add_book(self, book):
    self.books.append(book)
    self.no_of_books += 1

  def get_no_of_books(self):
    print(f"Total number of books: {self.no_of_books}")

library = Library(3, [
  "Programming PHP",
  "Python Crash Course",
  "Automate the Boring Stuff with Python",
  # "Fluent Python",
  # "Python Cookbook",
])

library.add_book("Effective Python")
library.all_books()
library.get_no_of_books()