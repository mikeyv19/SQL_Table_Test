from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Float)
    unit_name = db.Column(db.String(30))
    ingredient_name = db.Column(db.String(120))
    aisle_name = db.Column(db.String(30))
    aisle_id = db.Column(db.Integer)
    day_label = db.Column(db.String(10))

    def __repr__(self):
        return "<Shopping %r>" % self.ingredient_name


class Dshopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Float)
    unit_name = db.Column(db.String(30))
    ingredient_name = db.Column(db.String(120))
    aisle_name = db.Column(db.String(30))
    aisle_id = db.Column(db.Integer)
    day_label = db.Column(db.String(10))

    def __repr__(self):
        return "<Dshopping %r>" % self.ingredient_name


class Ingredient(db.Model):
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"))
    aisle_id = db.Column(db.Integer, db.ForeignKey("aisle.id"))
    ingredients = db.relationship("RecipeIngredient", backref="ingredient")

    def __str__(self):
        return "<Ingredient %r>" % self.name


class Aisle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    ingredients = db.relationship("Ingredient", backref="aisle")

    def __repr__(self):
        return "<Aisle %r>" % self.name


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(30))
    ingredients = db.relationship("Ingredient", backref="unit")

    def __repr__(self):
        return "<Aisle %r>" % self.name


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    ##Add tags - Dinner/App/Dessert? Chicken/Shrimp? Oven Only?
    ##Will also need Tag ID table

    def __repr__(self):
        return "<Recipe %r>" % self.name


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    iid = db.Column(db.Integer, db.ForeignKey("ingredient.id"))
    qty = db.Column(db.Float)
    unit_suffix = db.Column(db.String(50))

    def __repr__(self):
        return "<RecipeIngredient %r>" % self.rid


class Weekly_Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(100))

    def __repr__(self):
        return "<WeeklyRec %r>" % self.rid


def connect_db(app):
    db.app = app
    db.init_app(app)


# from main import Ingredient
# ingredient = Ingredient.query.all()
# for ingredient in ingredients:
#     print(ingredient.name)
#     print(ingredient.aisle.name)
