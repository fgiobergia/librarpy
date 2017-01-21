from progress_bar import ProgressBar
import json

class Book:
    def __init__(self, db, id):
        self.db = db
        self.id = id

        self.info = self.db.get_book_by_id(self.id)

        self.title = self.info['title']
        self.author = self.info['author']
        self.pages = self.info['pages']
        self.owned = self.info['owned']
        self.tags = json.loads(self.info['tags'])

        self.update_progress_list()


    def update_progress_list (self):
        self.progress_list = map(lambda c: { 'page': c['page'], 'date': c['date'] }, self.db.get_progress_list(self.id))

    def show_progress_bar (self):
        curr_page = self.progress_list[-1]['page']
        ProgressBar(curr_page, self.pages, length=30).show('lulzxxx')
