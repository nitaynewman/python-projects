from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# # first option
# # create a database connection
# db = sqlite3.connect('books-collection.db')

# # create a cursor
# cursor = db.cursor()

# # create a table
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# a few flask_sql commands = https://www.codecademy.com/articles/sql-commands

# # downloadsql os
# download the flask_sql browser for sqlite https://sqlitebrowser.org/dl/
# open db and click open db

# # adding data to db
# cursor.execute("INSERT INTO books VALUES(2, 'percy jacson', 'J. K. Rowling', '9.3')")
# db.commit()
# affter first run comment out the creating table part
# afterwords close the db then run again and reopen the db to see the changes

# # install package Flask_sqlalchemy:
# pip install -U Flask-SQLAlchemy

# # import Flask_SQLAlchemy:
# from flask_sqlalchemy import SQLAlchemy

# # doing everything we did with the package:
# # CREATE DATABASE
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# # Create the extension
# db = SQLAlchemy()
# # Initialise the app with the extension
# db.init_app(app)

# # CREATE TABLE
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)

    # # Optional: this will allow each book object to be identified by its title when printed.
    # def __repr__(self):
    #     return f'<Book {self.title}>'


# # Create table schema in the database. Requires application context.
# with app.app_context():
#     db.create_all()

# # CREATE RECORD
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


# # second and better option

# CREATING THE APP:
app = Flask(__name__, template_folder="templates")

# CREATING THE DATABASE:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"  
db = SQLAlchemy()
db.init_app(app)


# CREATING THE TABLE:
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context(): 
    db.create_all()


@app.route("/")
def home():
    # READING ALL RECORDS:
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATING A NEW RECORD:
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
