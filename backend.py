import sqlite3

class Database:


    def __init__(self, db):
        self.sql_conn = sqlite3.connect(db)
        self.sql_cursor = self.sql_conn.cursor()
        self.sql_cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(200), author VARCHAR(200), year_ YEAR, isbn VARCHAR(13))")
        self.sql_conn.commit()


    def delete_table(self):
        self.sql_cursor.execute("DROP TABLE IF EXISTS books")
        self.sql_conn.commit()


    def view_table(self):
        self.sql_cursor.execute("SELECT * FROM books")
        rows = self.sql_cursor.fetchall()
        self.sql_conn.commit()
        return rows


    def search_data(self, title="", author="", year_="", isbn=""):
        self.sql_cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year_=? OR isbn=?",
                           (title, author, year_, isbn))
        rows = self.sql_cursor.fetchall()
        self.sql_conn.commit()
        if not rows:
            return ("Could not find specified entry.",)
        return rows


    def insert_data(self, title, author, year_, isbn):
        self.sql_cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)", (None, title, author, year_, isbn))
        self.sql_conn.commit()


    def update_data(self, title, author, year_, isbn, book_id):
        self.sql_cursor.execute("UPDATE books SET title=?, author=?, year_=?, isbn=? WHERE book_id=?",
                           (title, author, year_, isbn, book_id))
        self.sql_conn.commit()


    def delete_data(self, book_id):
        self.sql_cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        self.sql_conn.commit()


    def __del__(self):
        self.sql_conn.close()


