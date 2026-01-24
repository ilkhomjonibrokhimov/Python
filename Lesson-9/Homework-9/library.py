class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        status = 'borrowed' if self.is_borrowed else 'available'
        return f"Title: {self.title}, Author: {self.author} ({status})"
    
class Member:
    Max_books = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < Member.Max_books

    def __str__(self):
        return f"{self.name}: {len(self.borrowed_books)}"

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member added: {member.name}")
    
    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)


        if not member:
            print("Member is not registered")
            return
        if not book:
            raise BookNotFoundException("There is no such book in the library")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed")
        if not member.can_borrow():
            raise MemberLimitExceededException('Borrowing limit reached (3)')
        
        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{book.title}")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print("Member not found")
            return
        
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        if not book:
            print("This book wasn't borrowed by the member")
            return
        
        book.is_borrowed = False
        member.borrowed_books.remove(book)
        print(f"{member.name} returned '{book.title}'")

library = Library()

book1 = Book("1984", "George Orwell")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Clean Code", "Robert C. Martin")
book4 = Book("Python Crash Course", "Eric Matthes")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

member1 = Member("Ali")
member2 = Member("Sara")

library.add_member(member1)
library.add_member(member2)

library.borrow_book('Ali', '1984')
library.borrow_book('Ali', 'The Alchemist')
library.borrow_book('Ali', 'Clean Code')
library.borrow_book('Sara', 'Python Crash Course')

library.return_book('Ali', "1984")
library.borrow_book('Sara', '1984')



    