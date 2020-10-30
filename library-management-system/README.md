# Library Management System

A system which can manage all the library functionalities and which can manage the asset collection in general.

### Requirements

- There are mainly two types of users librarian and the members / customers
- Member can Register themselves / Renew membership
- Members can borrow a book / reserve a book.
- Same book can have multiple copies in the library
- Every member can borrow at max 5 books at a time.
- Every member can borrow a book for at max 10 days.
- System should charge fine on the basis of the books.
- Librarian can add or delete the book.
- Members can search the book from the book catalogue.

### Use-Case Diagram

There are mainly three types of the users in the system. Those are:

1. Librarian
2. Member
3. System - which sends the notification to the users about the book availability / fine.

Basic Functionalities of the system would be:

- Register a new member / Renew Membership of the member.
- Add / Remove the Book.
- Add / Remove the Book Item.
- Borrow a book.
- Return the Book.
- Reserve a book.
- Search a book.

### Class Diagram

There are several classes in the system:

- Library: Central System which have these Functionalities.
- Book
- Book_Item
- Person
- Member
- Librarian
- Notification
- Lending
- Reservation
- Rack
- Fine

