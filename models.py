from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(120))
    aisle_name = db.Column(db.String(30))
    aisle_id = db.Column(db.Integer)

    def __repr__(self):
        return "<Shopping %r>" % self.ingredient_name


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


def connect_db(app):
    db.app = app
    db.init_app(app)


# from main import Ingredient
# ingredient = Ingredient.query.all()
# for ingredient in ingredients:
#     print(ingredient.name)
#     print(ingredient.aisle.name)
