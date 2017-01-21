from db import Db
from progress_bar import ProgressBar
from book import Book

db = Db('database.db')

hp = Book(db,1)
