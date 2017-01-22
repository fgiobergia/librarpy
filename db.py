import sqlite3
import json

class Db:
    def __init__ (self, filename):
        self.conn = sqlite3.connect(filename)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute ("PRAGMA foreign_key = ON;");

    def get_book_by_id (self, id):
        c = self.conn.execute ("SELECT * FROM Book WHERE id = ?;", (id,))
        return c.fetchone()

    def get_books_by_tag (self, tag):
        c = self.conn.execute ("SELECT id FROM Book WHERE tags LIKE '%\"'||?||'\"%';", (tag,))
        return c.fetchall()

    def get_books_by_tags (self, tags):
        # this could be done using a single query but, since the db is
        # supposed to be small, multiple calls to get_book_by_tag are acceptable
        books_set = map(lambda c: set(self.get_books_by_tag(c)), tags)
        return list(reduce (lambda c, v: c.intersection(v), books_set))

    def get_progress_list (self, id):
        c = self.conn.execute ("SELECT page, date FROM Progress WHERE id = ? ORDER BY date;", (id,))
        return c.fetchall()

    def add_book (self, title, author, pages, tags):
        self.conn.execute ("INSERT INTO Book (title, author, pages, tags) VALUES (?, ?, ?, ?);", (title, author, int(pages), json.dumps(tags)))
        self.conn.commit()
        c = self.conn.execute ("SELECT id FROM Book WHERE title = ?", (title,))
        return c.fetchone()


    def __del__ (self):
        self.close()

    def close (self):
        self.conn.close()

