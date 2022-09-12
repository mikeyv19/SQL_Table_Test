from pickle import NONE
from unicodedata import name
from flask import Flask, render_template
from models import (
    Ingredient,
    Aisle,
    Shopping,
    Recipe,
    RecipeIngredient,
    Unit,
    connect_db,
    db,
)
from forms import ManualShoppingForm, ShoppingForm, CreateIngredient

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


@app.route("/ingredients", methods=["GET", "POST"])
def ingredient_page():
    ingredient_list = Ingredient.query.order_by(Ingredient.name)
    x = db.session.query(Unit.label).order_by(Unit.label)
    x = [i[0] for i in x]
    form = CreateIngredient()
    form.unit.choices = [("")] + [(y) for y in x]
    a = db.session.query(Aisle.name).order_by(Aisle.name)
    a = [i[0] for i in a]
    form.aisle.choices = [("")] + [(b) for b in a]
    if form.validate_on_submit():
        uid = Unit.query.filter_by(label=form.unit.data).first()
        aid = Aisle.query.filter_by(name=form.aisle.data).first()
        update = Ingredient(name=form.name.data, unit_id=uid.id, aisle_id=aid.id)
        db.session.add(update)
        db.session.commit()
    return render_template(
        "ingredients.html",
        x=x,
        a=a,
        form=form,
        ingredient_list=ingredient_list,
    )


#    our_list = Ingredient.query.order_by(Ingredient.aisle_id)

# food = Ingredient.query.get(1)
# food = ingredient

# class Foods:
#     first_ingredient = Ingredient.query.get(1)
#     first_ingredient_aisle = Ingredient.query.get(1)
#     print(first_ingredient)
#     print(first_ingredient_aisle.aisle.name)
