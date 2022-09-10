from pickle import NONE
from unicodedata import name
from flask import Flask, render_template
from models import Ingredient, Aisle, connect_db, db

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food.db"

connect_db(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list():
    our_list = Ingredient.query.order_by(Ingredient.aisle_id)
    return render_template("list.html", our_list=our_list)



# my_ingredient.aisle.name
# my_aisle.ingredients

# from main import db
# db.create_all()

# from main import Aisle

# first = Aisle(id=1, name="Produce")
# second = Aisle(id=2, name="Seafood")
# third = Aisle(id=3, name="1")

# firstfood = Ingredient(id=1, name="Apple", aisle_id=1, )

# db.session.add(first)
# db.session.commit()

# Ingredient.query.all()
# Aisle.query.all()
