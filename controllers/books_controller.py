from flask import render_template, Blueprint, request
from models.book_list import books, reserve_book_list
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def index():
    return render_template('index.jinja', title='Library Book List', books=books)

@books_blueprint.route('/books/<index>')
def show_individual_book(index):
    index = books[int(index)]
    return render_template('individual_book.jinja', title="Book Details", index=index)

# I can't get this to work, and I think part of the problem is that too many things are called index...
# the crux of it is the line where I'm calling the reserve_book_list function ->
# I don't know how to indicate the class instance on which I want to perform that function
@books_blueprint.route('/books/<index>', methods=["POST"])
def update_reserve_book(index):
    index = books[int(index)]
    print(request.form)
    if request.form.get("reserve"):
        reserve_book_list(books[int(index)])
    # return redirect("/books/<index>")
    return "You have reserved this book"