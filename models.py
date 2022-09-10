from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

shopping_list = db.Table(
    "shopping_list",
    db.Column("ingredient_id", db.Integer, db.ForeignKey("ingredient.id")),
    db.Column("aisle_id", db.Integer, db.ForeignKey("aisle.id")),
)


class Shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    aisle = db.Column(db.String(50))

    def __repr__(self):
        return "<Shopping %r>" % self.name


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
# ingredient = Ingredient.post.query.all()
# for ingredient in ingredients:
#     print(ingredient.name)
#     print(ingredient.aisle.name)
