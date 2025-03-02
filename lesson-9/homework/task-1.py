import json
class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExceededException(Exception):
    pass
class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def to_dict(self):
        return {"title": self.title, "author": self.author, "is_borrowed": self.is_borrowed}
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["is_borrowed"])
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def to_dict(self):
        return {"name": self.name, "borrowed_books": [book.title for book in self.borrowed_books]}

    @classmethod
    def from_dict(cls, data, books_dict):
        member = cls(data["name"])
        member.borrowed_books = [books_dict[title] for title in data["borrowed_books"] if title in books_dict]
        return member
class Library:
    def __init__(self):
        self.books = {} 
        self.members = {} 
        self.load_data()
    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = Book(title, author)
            self.save_data()
            print(f"Book '{title}' by {author} added to the library.")
        else:
            print(f"Book '{title}' already exists.")
    def add_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)
            self.save_data()
            print(f"Member '{name}' added to the library.")
        else:
            print(f"Member '{name}' already exists.")
    def borrow_book(self, member_name, book_title):
        if member_name not in self.members:
            print(f"Member '{member_name}' not found.")
            return
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        book = self.books[book_title]
        member = self.members[member_name]
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"Member '{member_name}' has exceeded borrowing limit (3 books).")
        book.is_borrowed = True
        member.borrowed_books.append(book)
        self.save_data()
        print(f"'{book_title}' has been borrowed by '{member_name}'.")
    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            print(f"Member '{member_name}' not found.")
            return
        if book_title not in self.books:
            print(f"Book '{book_title}' does not exist in the library.")
            return
        member = self.members[member_name]
        book = self.books[book_title]
        if book not in member.borrowed_books:
            print(f"Book '{book_title}' was not borrowed by '{member_name}'.")
            return
        book.is_borrowed = False
        member.borrowed_books.remove(book)
        self.save_data()
        print(f"'{book_title}' has been returned by '{member_name}'.")
    def list_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book.title} by {book.author} ({status})")
    def list_members(self):
        print("\nLibrary Members:")
        for member in self.members.values():
            borrowed_titles = ", ".join(book.title for book in member.borrowed_books) if member.borrowed_books else "No books borrowed"
            print(f"- {member.name} (Borrowed: {borrowed_titles})")
    def save_data(self):
        data = {
            "books": {title: book.to_dict() for title, book in self.books.items()},
            "members": {name: member.to_dict() for name, member in self.members.items()}
        }
        with open("library_data.json", "w") as file:
            json.dump(data, file, indent=4)
    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                self.books = {title: Book.from_dict(details) for title, details in data.get("books", {}).items()}
                self.members = {name: Member.from_dict(details, self.books) for name, details in data.get("members", {}).items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = {}
            self.members = {}
if __name__ == "__main__":
    library = Library()
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_member("Alice")
    library.add_member("Bob")
    try:
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "Moby Dick")
    except Exception as e:
        print(f"Error: {e}")
    try:
        library.return_book("Alice", "1984")
        library.return_book("Alice", "Moby Dick") 
    except Exception as e:
        print(f"Error: {e}")

    library.list_books()
    library.list_members()
