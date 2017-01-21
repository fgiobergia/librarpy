CREATE TABLE Book (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL, 
        author TEXT NOT NULL,
        pages INTEGER NOT NULL,
        owned INTEGER DEFAULT 1, -- 0: false, 1: true
        tags TEXT
    );

CREATE TABLE Progress (
   id INTEGER, 
   page INTEGER,
   date INTEGER,
   FOREIGN KEY(id) REFERENCES Book(id),
   PRIMARY KEY(id, page)
);
