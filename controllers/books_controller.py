from flask import render_template, Blueprint, request
from models.book_list import books
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def index():
    return render_template('index.jinja', title='Library Book List', books=books)

@books_blueprint.route('/books/<index>')
def show_individual_book(index):
    index = books[int(index)]
    return render_template('individual_book.jinja', title="Book Details", index=index)

# @books_blueprint.route("/books/<index>")

# @tasks_blueprint.route('/tasks', methods=["POST"])
# def add_task():
#     print(request.form)
#     title = request.form["title"]
#     description = request.form["description"]
#     new_task = Task(title, description, False)
#     add_new_task(new_task)
#     return "Done"

# @events_blueprint.route('/events', methods=["POST"])
# def add_event():
#     print(request.form)
#     date = request.form["date"]
#     # split_date = date.split('-')
#     # date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
#     event_name = request.form["event_name"]
#     number_of_guests = request.form["number_of_guests"]
#     room_location = request.form["room_location"]
#     description = request.form["description"]
#     # alternative syntax -> recurring = True if 'recurring' in request.form else False
#     if request.form.get("recurring"):
#         recurring = request.form["recurring"]
#     else:   
#         recurring = False
#     new_event = Event(date, event_name, number_of_guests, room_location, description, recurring)
#     add_new_event(new_event)
#     return "Done"
# # or return redirect('/events')