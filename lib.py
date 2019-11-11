from flask import flask
app=flask(__name__)
db=SQLAlchemy(app)
from models import *

@app.route('/')
def index():
    return render.templete()


@app.route('/add', methods= ['POST'])
def add():
    book_id = request.get_json()['book_id']
    name=request.get_json()['name']
    author=request.get_json()['author']
    quantity=request.get_json()['quantity']
    # code.interact(local=dict(globals(), **locals()))
    try:
        Book=Book_trans(
            book_id=book_id,
            name=name,
            quantity=quantity
        )
        db.session.add(lib)
        db.session.commit()
        return "Book added. book id={}".format(Book.book_id)
    except Exception as e:
	    return(str(e))


@app.route('/get_all', methods = ['GET'])
def get_all():
   try:
        Book=Book_trans.query.all()
        return  jsonify([e.serialize() for e in Book])
    except Exception as e:
	    return(str(e))

@app.route('/user', methods = ['GET', 'POST'])
def user_info():
    user_name = request.get_json()['username']
    number=request.get_json()['number']
    


@app.route('/issue', methods = ['GET', 'POST'])
def issue_book():
    if Book_trans.query.filter(Book_trans.name==int(request.get_json['book_id'])).first().quantity==0:
        print('The Book Is Not Available')
    else:
        Book = get_bookby_serialno(int(request.get_json['book_id']))
        Book.quantity= quantity-1
        Book.serialno.remove(int(request.get_json['serialno']))
        Book.save()
        user.books.append(int(request.form['serialno']))
        user.save()

        

@app.route('/return', methoos =['GET', 'POST'])
def return_book():
    if not int(request.get_json['book_id']) in User.query.filter(User.username==request.get_json['username']).first().books:
        print("The User never issued this Book")
    else:
        user.books.remove(int(request.form['book_id']))
        user.save()
        book=get_bookby_serialno(int(request.form['serialno']))
        book.quantity=book.quantity+1
        book.serialno.append(int(request.form['serialno']))
        book.save()


if __name__ == "__main__":
    app.run(debug=True, port=3000)