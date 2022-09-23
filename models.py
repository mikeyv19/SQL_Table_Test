from time import process_time_ns
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
    icalories = db.Column(db.Float)
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)
    fiber = db.Column(db.Float)
    sugar = db.Column(db.Float)
    item_unit_size = db.Column(db.Float)  # How many units of item at store
    item_price = db.Column(db.Float)  # Price for full item at store
    u_price = db.Column(db.Float)
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
    course = db.Column(db.String(30))
    servings = db.Column(db.Float)
    serving_size = db.Column(db.String(30))
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)
    fiber = db.Column(db.Float)
    sugar = db.Column(db.Float)
    calories = db.Column(db.Float)
    total_cost = db.Column(db.Float)

    def __repr__(self):
        return "<Recipe %r>" % self.name

    def get_total_cost(self):
        x = [x.qty for x in RecipeIngredient.query.filter_by(rid=self.id).all()]
        y = [
            y.ingredient.u_price
            for y in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        tc = []
        for num1, num2 in zip(x, y):
            tc.append(num1 * num2)
        return sum(tc)

    def get_total_protein(self):
        x = [x.qty for x in RecipeIngredient.query.filter_by(rid=self.id).all()]
        y = [
            y.ingredient.protein
            for y in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        t = []
        for num1, num2 in zip(x, y):
            t.append(num1 * num2)
        return sum(t)

    def get_total_carbs(self):
        x = [x.qty for x in RecipeIngredient.query.filter_by(rid=self.id).all()]
        y = [
            y.ingredient.carbs
            for y in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        t = []
        for num1, num2 in zip(x, y):
            t.append(num1 * num2)
        return sum(t)

    def get_total_fat(self):
        x = [x.qty for x in RecipeIngredient.query.filter_by(rid=self.id).all()]
        y = [
            y.ingredient.fat
            for y in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        t = []
        for num1, num2 in zip(x, y):
            t.append(num1 * num2)
        return sum(t)

    def get_total_fiber(self):
        x = [x.qty for x in RecipeIngredient.query.filter_by(rid=self.id).all()]
        y = [
            y.ingredient.fiber
            for y in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        t = []
        for num1, num2 in zip(x, y):
            t.append(num1 * num2)
        return sum(t)

    def get_total_sugar(self):
        x = [x.qty for x in RecipeIngredient.query.filter_by(rid=self.id).all()]
        y = [
            y.ingredient.sugar
            for y in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        t = []
        for num1, num2 in zip(x, y):
            t.append(num1 * num2)
        return sum(t)

    def get_total_calories(self):
        a = [a.qty for a in RecipeIngredient.query.filter_by(rid=self.id).all()]
        p = [
            p.ingredient.protein
            for p in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        c = [
            c.ingredient.carbs
            for c in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        f = [
            f.ingredient.fat
            for f in RecipeIngredient.query.filter_by(rid=self.id).all()
        ]
        tp = []
        for num1, num2 in zip(a, p):
            tp.append((num1 * num2) * 4)
        tc = []
        for num1, num2 in zip(a, c):
            tc.append((num1 * num2) * 4)
        tf = []
        for num1, num2 in zip(a, f):
            tf.append((num1 * num2) * 9)
        gtl = (sum(tf))+(sum(tp))+(sum(tc))

        return gtl


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    iid = db.Column(db.Integer, db.ForeignKey("ingredient.id"))
    qty = db.Column(db.Float)
    unit_suffix = db.Column(db.String(50))
    cost = db.Column(db.Float)

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
