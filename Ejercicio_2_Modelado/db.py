import sqlite3
from classes import Book, Shelf

class Database:
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()  
        self.create_tables()
        
    def create_tables(self):
        """Crea las tablas de libros y estantes si no existen"""
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS shelves (
                               id INTEGER PRIMARY KEY,
                               location TEXT,
                               width INTEGER,
                               height INTEGER,
                               depth INTEGER,
                               maxCapacity INTEGER
                               )""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books (
                               ISBN INTEGER PRIMARY KEY,
                               name TEXT,
                               author TEXT,
                               genre TEXT,
                               price REAL,
                               shelf_id INTEGER,
                               FOREIGN KEY (shelf_id) REFERENCES shelves(id)
                               )""")
        
        self.conn.commit()
    
    def add_book(self, book: Book):
        """Agrega un libro a la base de datos"""
        self.cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", (book.ISBN, book.name, book.author, book.genre, book.price, book.shelf_id))
        self.conn.commit()
        
    def load_books(self) -> list:
        """Carga los libros de la base de datos"""
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return [Book(ISBN=row[0], name=row[1], author=row[2], genre=row[3], price=row[4], shelf_id=row[5]) for row in rows]
      
    def add_shelf(self, shelf: Shelf):
        """Agrega un estante a la base de datos"""
        self.cursor.execute("INSERT INTO shelves VALUES (?, ?, ?, ?, ?, ?)", (shelf.id, shelf.location, shelf.width, shelf.height, shelf.depth, shelf.maxCapacity))
        self.conn.commit()
        
    def load_shelves(self) -> list:
        """Carga los estantes de la base de datos"""
        self.cursor.execute("SELECT * FROM shelves")
        rows = self.cursor.fetchall()
        return [Shelf(id=row[0], location=row[1], width=row[2], height=row[3], depth=row[4], maxCapacity=row[5], books=[]) for row in rows]
      
    def close(self):
        """Cierra la conexión con la base de datos"""
        self.conn.close()

      
        