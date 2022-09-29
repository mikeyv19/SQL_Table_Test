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
    for_recipe = db.Column(db.String(120))

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

    def default_ingredient_unit(self):
        try:
            x = UnitIngredient.query.filter_by(iid=self.id).first()
            return x.unit.name
        except:
            return "Unknown"

    def traditional_ingredient_unit(self):
        try:
            x = (
                UnitIngredient.query.filter_by(iid=self.id)
                .order_by(UnitIngredient.multiplyer.desc())
                .all()
            )
            y = UnitIngredient.query.filter_by(iid=self.id).first()
            if x[0].unit.name not in ("ml", "g"):
                return x[0].unit.name
            else:
                return y.unit.name
        except:
            return "Unknown"

    def traditional_ingredient_multi(self):
        try:
            x = (
                UnitIngredient.query.filter_by(iid=self.id)
                .order_by(UnitIngredient.multiplyer.desc())
                .all()
            )
            y = UnitIngredient.query.filter_by(iid=self.id).first()
            if x[0].unit.name not in ("ml", "g"):
                return x[0].multiplyer
            else:
                return y.multiplyer
        except:
            return 1


class Aisle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    ingredients = db.relationship("Ingredient", backref="aisle")

    def __repr__(self):
        return "<Aisle %r>" % self.name


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.Integer, autoincrement=True)
    name = db.Column(db.String(30))
    ingredients = db.relationship("UnitIngredient", backref="unit")

    def __repr__(self):
        return "<Unit %r>" % self.name

    def count_unit(self):
        count = UnitIngredient.query.filter_by(uid=self.id).count()
        return count


class UnitIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iid = db.Column(db.Integer, db.ForeignKey("ingredient.id"))
    uid = db.Column(db.Integer, db.ForeignKey("unit.id"))
    name = db.Column(db.String(30))
    multiplyer = db.Column(db.Float)

    def __repr__(self):
        return "<UnitIngredient %r>" % self.id


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    course = db.Column(db.String(30))
    servings = db.Column(db.Float)
    serving_size = db.Column(db.String(30))
    tags = db.Column(db.Text)

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
        gtl = (sum(tf)) + (sum(tp)) + (sum(tc))

        return gtl


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    iid = db.Column(db.Integer, db.ForeignKey("ingredient.id"))
    qty = db.Column(db.Float)
    unit_suffix = db.Column(db.String(50))
    ingredient_color_tag = db.Column(db.String(20))

    def __repr__(self):
        return "<RecipeIngredient %r>" % self.rid

    def traditional_ingredient_multi1(self):
        x = (
            UnitIngredient.query.filter_by(iid=self.ingredient.id)
            .order_by(UnitIngredient.multiplyer.desc())
            .all()
        )
        y = UnitIngredient.query.filter_by(iid=self.ingredient.id).first()
        z = RecipeIngredient.query.filter_by(id=self.id).first()
        try:
            if x[0].unit.name not in ("ml", "g"):
                if x[0].unit.name in ("Cup(s)"):
                    if z.qty / x[0].multiplyer >= 0.25:
                        return x[0].multiplyer
                    elif x[1].unit.name in ("TBS"):
                        if z.qty / x[1].multiplyer >= 0.334:
                            return x[1].multiplyer
                    elif x[2].unit.name in ("tsp"):
                        return x[2].multiplyer
                elif x[0].unit.name in ("TBS"):
                    if z.qty / x[0].multiplyer >= 0.334:
                        return x[0].multiplyer
                    elif x[1].unit.name in ("tsp"):
                        return x[1].multiplyer
                elif x[1].unit.name in ("tsp"):
                    return x[1].multiplyer
                else:
                    return x[0].multiplyer
            else:
                return y.multiplyer
        except:
            return y.multiplyer

    def traditional_ingredient_unit1(self):
        x = (
            UnitIngredient.query.filter_by(iid=self.ingredient.id)
            .order_by(UnitIngredient.multiplyer.desc())
            .all()
        )
        y = UnitIngredient.query.filter_by(iid=self.ingredient.id).first()
        z = RecipeIngredient.query.filter_by(id=self.id).first()
        try:
            if x[0].unit.name not in ("ml", "g"):
                if x[0].unit.name in ("Cup(s)"):
                    if z.qty / x[0].multiplyer >= 0.25:
                        return x[0].unit.name
                    elif x[1].unit.name in ("TBS"):
                        if z.qty / x[1].multiplyer >= 0.334:
                            return x[1].unit.name
                    elif x[2].unit.name in ("tsp"):
                        return x[2].unit.name
                elif x[0].unit.name in ("TBS"):
                    if z.qty / x[0].multiplyer >= 0.334:
                        return x[0].unit.name
                    elif x[1].unit.name in ("tsp"):
                        return x[1].unit.name
                elif x[1].unit.name in ("tsp"):
                    return x[1].unit.name
                else:
                    return x[0].unit.name
            else:
                return y.unit.name
        except:
            return y.unit.name


class RecipeInstruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    instruction = db.Column(db.Text)
    instruction_color_tag = db.Column(db.String(20))

    def __repr__(self):
        return "<RecipeIngredient %r>" % self.rid


class Weekly_Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(100))
    qty = db.Column(db.Float)
    day = db.Column(db.String(100))
    servings = db.Column(db.Float)

    def __repr__(self):
        return "<WeeklyRec %r>" % self.rid

class WeeklyIngredientList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Float)
    unit_name = db.Column(db.String(30))
    ingredient_name = db.Column(db.String(120))
    day_label = db.Column(db.String(10))
    for_recipe = db.Column(db.String(120))

    def __repr__(self):
        return "<Shopping %r>" % self.ingredient_name


def connect_db(app):
    db.app = app
    db.init_app(app)


class RecipeMultiplyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)

    def __repr__(self):
        return "<RecipeMultiplyer %r>" % self.id


def connect_db(app):
    db.app = app
    db.init_app(app)


# from main import Ingredient
# ingredient = Ingredient.query.all()
# for ingredient in ingredients:
#     print(ingredient.name)
#     print(ingredient.aisle.name)
