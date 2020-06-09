import sqlite3

from xmlCleanDelete import extract_rating


# Run the `extract_rating()` method to grab the data from XML files
sample = extract_rating()

# Convert dictionary into a list of tuples
data = [(u, b, r) for u, b, r in zip(sample['user_id'], sample['book_id'], sample['rating'])]


# Innitiate connection with a database
conn = sqlite3.connect('/home/bexx/Projects/Aristarchus/data/books.db')

# Create a cursor
c = conn.cursor()


# Execute creation of a table
ratings_table_creation = "CREATE TABLE IF NOT EXISTS ratings (user_id INTEGER, book_id INTEGER, rating INTEGER);"
c.execute(ratings_table_creation)

# Execute injections
query = "INSERT INTO ratings (user_id, book_id, rating) VALUES (?, ?, ?)"
c.executemany(query, data)


# Commit the injection of the data and close the connection
conn.commit()
conn.close()



if __name__ == "__main__":
    print("All the data from the ratings XML folder has been injected into the Books.db ratings table")