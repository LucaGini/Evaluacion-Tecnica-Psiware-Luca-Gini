from dataclasses import dataclass
from typing import List

# Definición de clases utilizando dataclasses en vez de classes normales para simplificar la legibilidad del código
@dataclass
class Book:
    """Representa un libro con los siguientes atributos:"""
    ISBN: int
    name: str
    author: str
    genre: str
    price: float
    shelf_id: int 

@dataclass
class Shelf:
    """Representa un estante con los siguientes atributos:"""
    id: int
    location: str
    width: int
    height: int
    depth: int
    maxCapacity: int
    books: List[Book]
    
    def add_book(self, book: Book):
        """Agrega un libro al estante si hay espacio disponible"""
        if len(self.books) < self.maxCapacity:
            book.shelf_id = self.id # Asigno el id del estante al libro
            self.books.append(book)
        else:
            print("El estante está lleno")
            
    def book_count(self) -> int:
        """Retorna la cantidad de libros en el estante"""
        return len(self.books) 
      
    def fill_percentage(self) -> float:
        """Retorna el porcentaje de llenado del estante"""
        return (self.book_count()/self.maxCapacity)*100 if self.maxCapacity != 0 else 0
      
    def total_value(self) -> float:
        """Retorna el valor total de los libros en el estante"""
        return sum(book.price for book in self.books)
      
    def most_expensive_book(self) -> Book:
        """Retorna el libro más caro del estante"""
        return max(self.books, key=lambda book: book.price) if self.books else None 
      
    def books_alphabetically(self) -> List[Book]:
        """Retorna los libros ordenados alfabéticamente"""
        return sorted(self.books, key=lambda book: book.name) if self.books else [] 
      
    def books_by_genre(self, genre: str) -> List[Book]:
        """Retorna los libros de un género específico"""
        return [book for book in self.books if book.genre == genre] if self.books else []