from progress_bar import ProgressBar
import json

class Book:
    def __init__(self, db, id=None, title="", author="", pages=0, tags=[]):
        self.db = db

        if id == None: # create book first
            id = self.db.add_book(title, author, pages, tags)['id']

        self.id = id
        self.info = self.db.get_book_by_id(self.id)

        self.title = self.info['title']
        self.author = self.info['author']
        self.pages = self.info['pages']
        self.tags = json.loads(self.info['tags'])

        self.update_progress_list()

    def update_progress_list (self):
        self.progress_list = map(lambda c: { 'page': c['page'], 'date': c['date'] }, self.db.get_progress_list(self.id))
        if len(self.progress_list) == 0:
            self.progress_list = [ { 'page': 0, 'date': -1 } ]


    def show_progress_bar (self):
        curr_page = self.progress_list[-1]['page']

        title_length = 40
        title = self.title 
        if (len(self.title) > title_length):
            title = self.title[:title_length-3] + '...'
        else:
            title = self.title + ' ' * (title_length - len(self.title))
        ProgressBar(curr_page, self.pages, length=30).show(title)

