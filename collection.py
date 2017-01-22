from db import Db
from book import Book

class Collection:
    # create new collection filtering tags 
    def __init__(self, db, tags):
        self.db = db
        self.id_list = map(lambda r: r['id'], db.get_books_by_tags(tags))
        self.books_list = sorted(map(lambda b: Book(db,b), self.id_list), key=lambda b: b.title)

    def show_books(self):
        for book in self.books_list:
            book.show_progress_bar()
