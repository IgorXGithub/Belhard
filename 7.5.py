class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return self.year > other.year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"




class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __contains__(self, book):
        return book in self.books

# Пример использования класса Library
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library.add_book(book1)
library.add_book(book2)


print(book1 in library)  # True
print(book2 in library)  # True
