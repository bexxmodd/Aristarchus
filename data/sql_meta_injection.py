import sqlite3
from xmlCleanDelete import extract_meta


s = extract_meta()

                # metadata['book_id']
                # metadata['title'].
                # metadata['author'].
                # metadata['isbn13'].
                # metadata['published']
                # metadata['pages'].
                # metadata['avg_rating'].
                # metadata['count'].
                # metadata['lang']
                # metadata['cover_url']
# data = [(int(b), t, a, int(i), d, int(p), float(r), int(c), l) for b, t, a, i, d, p, r, c, l in zip(s['book_id'], s['title'], s['author'], s['isbn13'],
#                                                         s['published'], s['pages'], s['avg_rating'], s['count'], s['lang'])]
dat = []
for b, t, a, i, d, p, r, c, l in zip(s['book_id'], s['title'], s['author'], s['isbn13'], s['published'],
                                        s['pages'], s['avg_rating'], s['count'], s['lang']):
    if None in (b, i, p, r, c):
        dat.append(None)
    else:
        dat.append((int(b), t, a, int(i), d, int(p), float(r), int(c), l))

print(dat)
# # Innitiate connection with a database
# conn = sqlite3.connect('/home/bexx/Projects/Aristarchus/data/books.db')

# # Create a cursor
# c = conn.cursor()

# meta_table_create = "CREATE TABLE IF NOT EXISTS metadata (book_id INT PRIMARY KEY, title TEXT, author TEXT, isbn13 TEXT, published TEXT, pages TEXT, avg_rating DOUBLE, count INT, lang TEXT)"
# c.execute(meta_table_create)