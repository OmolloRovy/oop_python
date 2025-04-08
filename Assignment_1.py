# Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author} costs ${self.price}"

    def read(self):
        return f"Reading '{self.title}' by {self.author}..."

# EBook class inherits from Book
class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def __str__(self):
        return f"'{self.title}' by {self.author}, file size: {self.file_size}MB, costs ${self.price}"

    def download(self):
        return f"Downloading '{self.title}' by {self.author}..."

# Creating an instance of Book
physical_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
print(physical_book)  # This will call the __str__() method
print(physical_book.read())  # Simulates reading the book

# Creating an instance of EBook
ebook = EBook("1984", "George Orwell", 7.99, 2.5)
print(ebook)  # This will call the __str__() method, including the file size
print(ebook.download())  # Simulates downloading the ebook
