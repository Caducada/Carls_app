from flask import Flask, render_template, url_for, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from config import db, fake_people, Person
from sqlalchemy import column
from functools import lru_cache
import time

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:password@localhost:3306/vips"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["REMEMBER_COOKIE_SAMESITE"] = "strict"
app.config["SESSION_COOKIE_SAMESITE"] = "strict"
db.app = app
db.init_app(app)

@lru_cache(maxsize=50, typed=False)
def get_people(search_string):
    return Person.query.filter(Person.name.like(f"%{search_string}%"))


@app.route("/", methods=["GET", "POST"])
def index():
    search = request.form.get("search", "").lower().replace(" ", "")
    current_page = request.args.get("current_page", 1)
    old_search = request.args.get("old_search", "")
    if len(old_search):
        search = old_search
    if search:
        pre_search = get_people.cache_info().hits
        pagination = get_people(search).paginate(
            page=int(current_page), per_page=20, error_out=False
        )
        post_search = get_people.cache_info().hits
        people = pagination.items
        page_count = pagination.pages
        if pre_search == post_search:
            time.sleep(5)
    else:
        pagination = get_people(search).paginate(
            page=int(current_page), per_page=20, error_out=False
        )
        people = pagination.items
        page_count = pagination.pages
    if page_count == 0:
        page_count = 1

    return render_template(
        "index.html",
        people=people,
        search=search,
        current_page=int(current_page),
        page_count = int(page_count),
    )
    
@app.route("/person_page/<ID>", methods=["GET", "POST"])
def person_page(ID):
    person = Person.query.filter_by(ID=ID).first()
    return render_template(
        "person_page.html",
        person = person
    )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()
    with app.app_context():
        if len(Person.query.all()) < 10000:
            fake_people()
    app.run(debug=True)
