from flask import render_template, request, flash, redirect, url_for, session
from app import app
from services.book_service import book_service
from services.user_service import user_service
from services.review_service import review_service
from services.feedback_service import feedback_service
from services.genre_service import genre_service

@app.route("/", methods=["GET"])
def render_index():
  books = book_service.get_visible_books()
  genres = genre_service.get_genres()
  return render_template("index.html", books=books, genres=genres)

@app.route("/delete", methods=["POST"])
def delete_book():
  id_to_delete = request.form.get("delete")
  csrf_token=request.form.get('csrf_token')
  delete = book_service.delete_book(id_to_delete, csrf_token)
  delete_reviews = review_service.delete_reviews_of_book(id_to_delete, csrf_token)
  if delete and delete_reviews:
    flash("Poisto onnistui")
  else:
    flash("Poisto ei onnistunut")
  return redirect_to_index()

@app.route("/favourite_book", methods=["POST"])
def favourite_book():
  try:
    id_to_fav = request.form.get("favourite")
    id_to_unfav = request.form.get("unfavourite")
    csrf_token=request.form.get('csrf_token')
    user_service.fav_book(id_to_fav, id_to_unfav, csrf_token)
    return redirect_to_index()
  except Exception as error:
      flash(str(error))
      return redirect_to_index()

@app.route("/book/<int:book_id>/review/delete", methods=["POST"])
def delete_review(book_id):
  id_to_delete = request.form.get("delete")
  csrf_token=request.form.get('csrf_token')

  delete = review_service.delete_review(id_to_delete, csrf_token)
  if delete:
    flash("Poisto onnistui")
  else:
    flash("Poisto ei onnistunut")
  return redirect_to_book(book_id)

@app.route("/book/<int:book_id>/review/like", methods=["POST"])
def favourite_review(book_id):
  try:
    id_to_fav = request.form.get("favourite")
    id_to_unfav = request.form.get("unfavourite")
    csrf_token=request.form.get('csrf_token')
    user_service.fav_review(id_to_fav, id_to_unfav, csrf_token)
    return redirect_to_book(book_id)
  except Exception as error:
      flash(str(error))
      return redirect_to_book(book_id)

@app.route("/book/<int:book_id>", methods=["GET"])
def render_book(book_id):

    try: 
      book = book_service.get_info(book_id)
      reviews = review_service.get_visible_reviews(book_id)
      genres = genre_service.get_genres_of_book(book.genres)
      statistics = review_service.get_statistics(book_id)
      return render_template("book.html", reviews=reviews, book=book, genres=genres, statistics=statistics)
    except Exception as error:
      flash(str(error))
      return redirect_to_index()

@app.route("/type/<int:genre_id>/<string:genre_name>", methods=["GET"])
def render_type_books(genre_id, genre_name):
    try: 
      books = book_service.get_books_by_genre(genre_id)
      return render_template("books_by_genre.html", books=books, genre=genre_name)
    except Exception as error:
      flash(str(error))
      return redirect_to_index()

@app.route("/book/<int:book_id>/review/add", methods=["POST"])
def add_review(book_id):
  try:
    stars = request.form.get("stars")
    review = request.form.get("review")
    csrf_token=request.form.get('csrf_token')
    review_service.add_review(book_id, stars, review, csrf_token)
    return redirect_to_book(book_id)
  except Exception as error:
    flash(str(error))
    return redirect_to_book(book_id)


@app.route("/search", methods=['GET'])
def search():
  query = request.args["search"]
  option = request.args['search_option']
  books = book_service.get_searched_books(query, option)
  return render_template("search.html", books=books, option=option, query=query)

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
  cover = request.form.get("cover")

  csrf_token=request.form.get('csrf_token')
  try:
    book_service.add_new_book(name, author, description, genres, csrf_token, cover )
    return redirect_to_index()

  except Exception as error:
    flash(str(error))
    return redirect_to_add_book()

@app.route("/add_book/add_genre", methods=["POST"])
def add_new_genre():
  name = request.form.get("name")
  csrf_token=request.form.get('csrf_token')
  try:
    genre_service.add_genre(name, csrf_token)
    return redirect_to_add_book()
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
  try:
    user_service.create_user(username, password, password_confirmation)
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

  try:
    username= request.form.get("username")
    password = request.form.get("password")
    user_service.login(username, password)
    flash(str("Kirjauduit sisään"))
    return redirect_to_index()
  except Exception as error:
    flash(str(error))
    return redirect_to_login()

@app.route("/feedback", methods=["GET"])
def render_feedback():
  return render_template("feedback.html")


@app.route("/feedback", methods=["POST"])
def give_feedback():
  try:
    feedback = request.form.get("feedback")
    csrf_token=request.form.get('csrf_token')
    feedback_service.add_feedback(feedback, csrf_token)
    return redirect_to_index()
  except Exception as error:
    flash(str(error))
    return redirect_to_feedback()
 

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

def redirect_to_feedback():
  return redirect(url_for("render_feedback"))