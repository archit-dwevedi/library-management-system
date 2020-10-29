from enum import Enum

class Constants:
    self.Max_Book_Allowed_For_Lend = 5
    self.Max_Days_Allowed_For_Lend = 10


class BookStatus(Enum):
    Availiable, Borrowed, Reserved = 1, 2, 3


class MembershipStatus(Enum):
    Active, Inactive = 1, 2



class Person:
    def __init__(self, name, address, contact, email):
        self.__name = name
        self.__address = address
        self.__contact = contact 
        self.__email = email


class Member(Person):
    def __init__(self, name, address, contact, email):
        super().__init__(name, address, contact, email)
        self.__booksBorrowed = 0


    def borrow_book(self, bookItem):
        if not bookItem.status == BookStatus.Availiable:
            print("Sorry, this book is not availiable")
            return False

        if self.getbooksBorrowed() == Constants.Max_Book_Allowed_For_Lend:
            print("Sorry, you cannot lend the book")
            return False

        isReserved = ReservedItems.filter(bookItem)

        if isReserved:
            print("Sorry, Book is reserved")
            return False

        self.update_books_borrowed(self.get_books_borrowed()+1)
        bookItem.set_status(BookStatus.Availiable)
        BookLending.create_lending_order(bookItem, member)
        

    def return_book(self, bookItem):
        # Update the count of user

        # Change book Status

        # Send Notification if the book is reserved

    def reserve_book(self, bookItem):
        pass


class BookLending:
    def __init__(self):
        self.__maximum_order = 0

    def create_lending_order(self, bookItem, member):
        pass



class Librarian(Person):
    def __init__(self):
        pass

    def add_book(self, bookItem):
        pass

    def delete_book(self, bookItem):
        pass
    
    def reserve_book(self, bookItem):
        pass

class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__price = price
        self.__author = author

class BookItem:
    def __init__(self, book, bookItemId, status, rack):
        self.__book = book
        self.__bookItemId = bookItemId
        self.__status = status
        self.__rack = rack


class Rack:
    def __init__(self, Id, location):
        self.__id = Id
        self.__location = location

class Notification:
    def __init__(self, id, message, member):
        self.__message = message
        self.__id = id
        self.__member = member


    def notify_using_email(self):
        pass

    def notify_using_whatsapp(self):
        pass

class Fine:
    def __init__(self, book, extraDaysLended, member):
        self.__book = book
        self.__member = member
        self.__extraDaysLended = extraDaysLended

