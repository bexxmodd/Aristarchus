import sqlite3
import numpy as np
from xmlCleanDelete import extract_meta


s = extract_meta()

# Extrapolate the data as the set of values into the list.
data = []
for b, t, a, i, y, p, r, c, lan, u in zip(s['book_id'], s['title'], s['author'], s['isbn13'], s['published'], s['pages'], s['avg_rating'], s['count'], s['lang'], s['cover_url']):
    data.append((int(b), t, a, i, y, int(p or 0), float(r or 0), int(c or 0), lan, u))

# Innitiate connection with a database.
conn = sqlite3.connect('/home/bexx/Projects/Aristarchus/data/books.db')

# Create a cursor.
c = conn.cursor()

# Create metadata table.
create_mt = "CREATE TABLE IF NOT EXISTS metadata (book_id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn13 TEXT, published TEXT, pages INTEGER, avg_rating REAL, count INT, lang TEXT, cover_url TEXT)"
c.execute(create_mt)

# Inject data into the metadata table.
q = "INSERT INTO metadata (book_id, title, author, isbn13, published, pages, avg_rating, count, lang, cover_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
c.executemany(q, data)

# Commit and close the connection.
conn.commit()
conn.close()

if __name__ == "__main__":
    print("All the data from the metadata XML folder has been injected into the Books.db metadata table")