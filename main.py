from pickle import NONE
from unicodedata import name
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food.db"

db = SQLAlchemy(app)


class Ingredient(db.Model):
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    aisle_id = db.Column(db.Integer, db.ForeignKey("aisle.id"))

    def __repr__(self):
        return "<Ingredient %r>" % self.name


class Aisle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    ingredients = db.relationship("Ingredient", backref="aisle")

    def __repr__(self):
        return "<Aisle %r>" % self.name


class Foods:
    first_ingredient = Ingredient.query.get(1)
    first_ingredient_aisle = Ingredient.query.get(1)
    print(first_ingredient)
    print(first_ingredient_aisle.aisle.name)


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
