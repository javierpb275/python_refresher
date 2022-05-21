class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("The Treasure Island")

shelf = BookShelf(book, book2)

print(shelf)  # BookShelf with 2 books.
print(shelf.books)  # (<__main__.Book object at 0x000002164058FFD0>, <__main__.Book object at 0x000002164058FF70>)
