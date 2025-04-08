class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):# In Python, __str__ is a special method used to define a string representation of an object.
        return f"'{self.title}' by {self.author} costs ${self.price}"

    def read(self):
        return f"Reading '{self.title}' by {self.author}..."

class EBook(Book):  # Inheriting from Book
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def __str__(self):
        return f"'{self.title}' by {self.author}, file size: {self.file_size}MB, costs ${self.price}"

    def download(self):
        return f"Downloading '{self.title}' by {self.author}..."
