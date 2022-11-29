from flask import render_template, request, flash, redirect, url_for, session
from app import app
from services.book_service import book_service
from services.user_service import user_service
from services.review_service import review_service
from services.genre_service import genre_service

@app.route("/", methods=["GET"])
def render_index():
    visible_books = book_service.get_visible_books()
    return render_template("index.html", books=visible_books)

@app.route("/", methods=["POST"])
def delete_book():
    id_to_delete = request.form["delete"]
    delete = book_service.delete_book(id_to_delete)
    delete_reviews = review_service.delete_reviews_of_book(id_to_delete)
    if delete and delete_reviews:
        flash("Poisto onnistui")
    else:
        flash("Poisto ei onnistunut")
    return redirect_to_index()

@app.route("/book/<int:book_id>", methods=["GET", "POST"])
def render_book(book_id):
  if request.method == 'GET': 
    try: 
        book = book_service.get_info(book_id)
        reviews = review_service.get_visible_reviews(book_id)
        genres = genre_service.get_genres_of_book(book.genres)
        return render_template("book.html", reviews=reviews, book=book, genres=genres)
    except Exception as error:
        flash(str(error))
        return redirect_to_index()
  elif request.method == 'POST':
    stars = request.form.get("stars")
    review = request.form.get("review")
    try:
        book_service.add_stars(book_id, stars)
        review_service.add_review(user_id=session["user_id"], username=session["username"], book_id=book_id, stars=stars, review=review)
        return redirect_to_book(book_id)
    except Exception as error:
      flash(str(error))
      return redirect_to_book(book_id)

@app.route("/book/<int:book_id>/review", methods=["POST"])
def delete_review(book_id):

    if request.form['delete']:
      id_to_delete = request.form["delete"]
      delete = review_service.delete_review(id_to_delete)
      if delete:
          flash("Poisto onnistui")
      else:
          flash("Poisto ei onnistunut")
      return redirect_to_book(book_id)

@app.route("/search")
def search():
    query = request.args["search"]
    books = book_service.get_searched_books(query)
    return render_template("search.html", books=books)

@app.route("/add_book", methods=["GET"])
def render_add_book():
    genres = genre_service.get_genres()
    return render_template("add_book.html", genres=genres)


@app.route("/add_book", methods=["POST"])
def add_new_book():
    name = request.form.get("name")
    author = request.form.get("author")
    description = request.form.get("description")
    genres = list(map(int, request.form.getlist("genres"))) 
    admin = session["admin"]
    try:
        book_service.add_new_book(admin, name, author, description, genres )
        return redirect_to_index()

    except Exception as error:
        flash(str(error))
        return redirect_to_add_book()



@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_new_user():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")
    role = 0

    try:
        user_service.create_user(username, password, password_confirmation, role)
        user_service.login(username, password)
        flash(str("Käyttäjätunnus on rekisteröity."))
        return redirect_to_index()
    except Exception as error:
        flash(str(error))
        return redirect_to_register()

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def try_login():
    username= request.form.get("username")
    password = request.form.get("password")

    try:
        user_service.login(username, password)
        flash(str("Kirjauduit sisään"))
        return redirect_to_index()
    except Exception as error:
        flash(str(error))
        return redirect_to_login()

@app.route("/logout")
def logout():
    user_service.logout()
    flash(str("Kirjauduit ulos"))
    return redirect_to_index()


def redirect_to_index():
    return redirect(url_for("render_index"))

def redirect_to_register():
    return redirect(url_for("render_register"))

def redirect_to_login():
    return redirect(url_for("render_login"))

def redirect_to_add_book():
    return redirect(url_for("render_add_book"))

def redirect_to_book(book_id):
    return redirect(url_for("render_book", book_id=book_id))