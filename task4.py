class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"'{self.title}' by {self.author}, published in {self.year_published}.")

# Creating three book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Displaying their details
book1.describe()
book2.describe()
book3.describe()
