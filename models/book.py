class Book():

    def __init__(self, input_title, input_author, input_genre):
        self.title = input_title
        self.author = input_author
        self.genre = input_genre
        self.in_stock = True
    
    def reserve_book(self):
        self.in_stock = False