CREATE TABLE Book (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL UNIQUE, 
        author TEXT NOT NULL,
        pages INTEGER NOT NULL,
        tags TEXT
    );

CREATE TABLE Progress (
   id INTEGER, 
   page INTEGER,
   date INTEGER,
   FOREIGN KEY(id) REFERENCES Book(id),
   PRIMARY KEY(id, page)
);
