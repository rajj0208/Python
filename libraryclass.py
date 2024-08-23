class Library:
    def __init__(self):
        self.no_books = 0
        self.books = []
    def addbook(self, bookName):
        self.books.append(bookName)
        self.no_books = self.no_books + 1
    def showBook(self):
        for b in self.books:
            print(b)


l1 = Library()

l1.addbook("Operating system")
l1.addbook("Compiler Desing")
l1.addbook("DBMS")
l1.addbook("Computer Organization")

print("The number of books in the Library is ", l1.no_books)
l1.showBook()