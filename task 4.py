class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: '{self.title}' by {self.author}, published in {self.year_published}.")



book4 = Book("Pride and Prejudice", "Jane Austen", 1813)
book5 = Book("Moby-Dick", "Herman Melville", 1851)
book6 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)

book4.describe()
book5.describe()
book6.describe()

