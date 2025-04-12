from typing import List
from copy import deepcopy

class Book:
    """
    Book class, which contains the title and author of the book..
    """
    def __init__(self, title: str, author: str) -> None :
        self.__title = title
        self.__author = author

    def get_title(self) ->str :
        return self.__title
    
    def set_title(self, title: str) ->None :
        self.__title = title

    def get_author(self) ->str :
        return self.__author
    
    def set_author(self, author: str) ->None:
        self.__author = author

    def __str__(self):
        return f"{self.__title} by {self.__author}"

class Library:
    """
    Library class that manages a collection of books.
    """
    def __init__(self) ->None:
        self.__books = []  

    def add_book(self, title: str, author: str)->None:
        """
        Adds a new book to the library.

         title: Book title (str)
         author: Author name (str)
        """
        new_book = Book(title=title, author=author)
        self.__books.append(new_book)

    def list_books(self) -> str:  
        """
        Prints a list of all the books in the library.
        """
        for book in self.__books:
            print(book)

    def __str__(self)-> str:
        """
        Returns the list of books in the library.
        """
        return self.list_books()

library = Library()
library.add_book("Chashmhayash", "Bozorgh Alavi")
library.add_book("A Man Called Ove", "Fredrik Backman")
library.list_books()