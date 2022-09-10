from pickle import NONE
from unicodedata import name
from flask import Flask, render_template
from models import Ingredient, Aisle, Shopping, connect_db, db

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
