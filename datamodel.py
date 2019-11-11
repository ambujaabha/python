from lib import db
class Book_trans:

    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    quantity = db.Column(db.Integer())

    def __init__(self, book_list, book_id, name):
        self.book_list=book_list
        self.book_id=book_id
        self.name=name
        self.quantity=quantity
        self.lend_dict={}
    
    def display(self):
        for book in book_list:
            return book
    
    def lend_book(self, user, book):
        if book not in self.lend_dict.keys():
            return self.lend_dict.update({book:user})
        else:
            return False

    def add_book(self, book):
        self.book_list.append(book)


    def return_book(self, book):
        self.lend_dict.pop(book)


class User:
    
    username = db.Column(db.String())
    number = db.Column(db.Integer())
    Id = db.Column(db.Book_trans(), foreign_key=True)

    def __init__(self, username, number,):
        self.username = username
        self.number = number


class Transactions:
    



