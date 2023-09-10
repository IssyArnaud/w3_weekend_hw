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

# print(books[0].in_stock)
# book_01.reserve_book()
# print(book_01.in_stock)
def reserve_book_list(book):
    book.reserve_book()
    # print(book.in_stock)

# print(books[0].in_stock)
# reserve_book_list(books[0])
