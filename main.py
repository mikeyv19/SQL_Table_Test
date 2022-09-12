from pickle import NONE
from unicodedata import name
from flask import Flask, render_template
from models import Ingredient, Aisle, Shopping, Recipe, RecipeIngredient, connect_db, db
from forms import ManualShoppingForm, ShoppingForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "sk"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food.db"

connect_db(app)


@app.route("/")
def index():
    return render_template("index.html")


#################
## RECIPE LIST ##
#################
@app.route("/recipe_list")
def recipe_list():
    recipe_list = Recipe.query.order_by(Recipe.name)
    return render_template("recipe_list.html", recipe_list=recipe_list)


#################
## RECIPE PAGE ##
#################
@app.route("/recipe/<int:id>")
def recipe(id):
    r = Recipe.query.get_or_404(id)
    title = r.name
    x = 1
    iquery = RecipeIngredient.query.filter_by(rid=id).all()
    return render_template("recipe.html", r=r, title=title, x=x, iquery=iquery)


#################
# SHOPPING LIST #
#################
@app.route("/list", methods=["GET", "POST"])
def list():
    our_add = Shopping.query.order_by(Shopping.aisle_id)
    names = db.session.query(Ingredient.name).order_by(Ingredient.name)
    names = [i[0] for i in names]
    form = ShoppingForm()
    form.name.choices = [("")] + [(name) for name in names]
    item = None
    form2 = ManualShoppingForm()
    if form.validate_on_submit():
        u1 = Ingredient.query.filter_by(name=form.name.data).first()
        update = Shopping(
            ingredient_name=u1.name,
            qty=form.aqty.data,
            unit_name=u1.unit.label,
            aisle_name=u1.aisle.name,
            aisle_id=u1.aisle_id,
        )
        db.session.add(update)
        db.session.commit()
        return render_template(
            "list.html", form=form, form2=form2, item=item, name=name, our_add=our_add
        )
    if form2.validate_on_submit():
        update = Shopping(
            ingredient_name=form2.item.data,
            qty=form2.bqty.data,
            unit_name="",
            aisle_name="Unknown",
            aisle_id=0,
        )
        db.session.add(update)
        db.session.commit()
        form2.item.data = ""
        return render_template(
            "list.html", form=form, form2=form2, item=item, name=name, our_add=our_add
        )
    else:
        return render_template(
            "list.html", form=form, form2=form2, item=item, name=name, our_add=our_add
        )


# @app.route("/list", methods=["GET", "POST"])
# def list():
#     item = None
#     form = ShoppingForm()
#     if form.validate_on_submit():
#         try:
#             u1 = Ingredient.query.filter_by(name=form.item.data).first()
#             update = Shopping(
#                 ingredient_name=u1.name, aisle_name=u1.aisle.name, aisle_id=u1.aisle_id
#             )
#             db.session.add(update)
#             db.session.commit()
#             our_add = Shopping.query.order_by(Shopping.aisle_id)
#             return render_template("list.html", item=item, form=form, our_add=our_add)
#         except:
#             update = Shopping(
#                 ingredient_name=form.item.data, aisle_name="Unknown", aisle_id=0
#             )
#             our_add = Shopping.query.order_by(Shopping.aisle_id)
#             db.session.add(update)
#             db.session.commit()
#             return render_template("list.html", item=item, form=form, our_add=our_add)
#     else:
#         return render_template("list.html", item=item, form=form)


#    our_list = Ingredient.query.order_by(Ingredient.aisle_id)

# food = Ingredient.query.get(1)
# food = ingredient

# class Foods:
#     first_ingredient = Ingredient.query.get(1)
#     first_ingredient_aisle = Ingredient.query.get(1)
#     print(first_ingredient)
#     print(first_ingredient_aisle.aisle.name)
