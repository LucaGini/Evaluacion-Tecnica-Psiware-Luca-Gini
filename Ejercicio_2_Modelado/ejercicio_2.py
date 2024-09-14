"""
Resolución de ejercicio 2 --> Modelado
"""
from classes import Book, Shelf
from db import Database
      
# Ejemplo de uso

if __name__ == "__main__": # El código se ejecuta solo si se ejecuta el archivo directamente y no si se importa desde otro archivo
    
    # Creo una conexión con la db de sqlite3
    db = Database()
    
    # Cargo los estantes de la db
    shelves = db.load_shelves()
    
    # Si no hay estantes, creo uno
    if not shelves:
        shelf1 = Shelf(1, "A1", 100, 200, 50, 8, [])
        db.add_shelf(shelf1)
        shelves = [shelf1] 
    
    # Cargar los libros de la db
    books_db = db.load_books()
    
    # Si no hay libros en la db, creo algunos y los agrego
    if not books_db:
        books = [
            Book(1, "El principito", "Antoine de Saint-Exupéry", "Infantil", 500, 1),
            Book(2, "El señor de los anillos", "J.R.R. Tolkien", "Fantasía", 1000, 1),
            Book(3, "Harry Potter", "J.K. Rowling", "Fantasía", 800, 1),
            Book(4, "Game of Thrones", "George R.R. Martin", "Fantasía", 1200, 1),
            Book(5, "El código Da Vinci", "Dan Brown", "Misterio", 900, 1)
        ]
        
        for book in books:
            db.add_book(book)
        
        books_db = books # Actualizo la lista de libros con los nuevos libros

    # Asocio los libros con sus respectivos estantes
    for shelf in shelves:
        shelf.books = [book for book in books_db if book.shelf_id == shelf.id]

    # Utilizo el primer estante para mostrar la información
    shelf1 = shelves[0]
        
    # Muestro información requerida por el enunciado
    print(f"\nLibros en el estante: {shelf1.book_count()}")
    
    print(f"\nPorcentaje de llenado: {shelf1.fill_percentage()}%")
    
    print(f"\nValor total de los libros: {shelf1.total_value()}")
    
    most_expensive = shelf1.most_expensive_book()
    if most_expensive:
        print(f"\nLibro más caro: {most_expensive.name}")
    else:
        print("\nNo hay libros en el estante")
        
    print(f"\nLibros ordenados alfabéticamente: ")
    for i, book in enumerate(shelf1.books_alphabetically()):
        print(f"{i+1}. {book.name}")
        
    fantasy_books = shelf1.books_by_genre("Fantasía") 
    if fantasy_books:
        print("\nLibros de fantasía: ")
        for i, book in enumerate(fantasy_books):
            print(f"{i+1}. {book.name} de {book.author}, Precio: {book.price}") 
    else:
        print("\nNo hay libros de fantasía en el estante")
        
    
    # Cierro la conexión con la db
    db.close()


    
    