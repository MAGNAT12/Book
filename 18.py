class Book:

    def __init__(self, name_book, author, year_of_issue) -> None:
        self.name_book = name_book
        self.author = author
        self.year_of_issue = year_of_issue
    
    def name(self):
        print(self.name_book, self.author, self.year_of_issue)


a = Book("Война и мир", "Торстой", "1500")
a.name()
