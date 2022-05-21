class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book('{self.name}', '{self.book_type}', {self.weight})>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("The Treasure Island", 1500)

print(Book.TYPES)  # ('hardcover', 'paperback')
print(book)  # <Book('Harry Potter', 'hardcover', 1600)>
print(book2)  # <Book('The treasure Island', 'paperback', 1500)>
