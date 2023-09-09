from models.book import Book

book_01 = Book("Nineteen Eighty-Four", "George Orwell", "Dystopian fiction")
book_02 = Book("A Farewell to Arms", "Ernest Hemmingway", "War fiction")
book_03 = Book("Brideshead Revisited", "Evelyn Waugh", "Classic fiction")

books = [book_01, book_02, book_03]

def add_new_book(book):
    books.append(book)

# book_04 = Book("Emma", "Jane Austen", "Classic Fiction")
# add_new_book(book_04)

def remove_book(book):
    books.remove(book)

# remove_book(book_04)