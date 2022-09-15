from itertools import groupby
from pickle import NONE
from unicodedata import name
from flask import Flask, render_template, request
from models import (
    Ingredient,
    Aisle,
    Shopping,
    Dshopping,
    Recipe,
    RecipeIngredient,
    Unit,
    connect_db,
    db,
)
from forms import ManualShoppingForm, ShoppingForm, CreateIngredient, SelectRecipe
from sqlalchemy import func


app = Flask(__name__)

app.config["SECRET_KEY"] = "sk"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food.db"

connect_db(app)


@app.route("/")
def index():
    return render_template("index.html")


#################
## Weekly PLan ##
#################
@app.route("/weekly_plan")
def weekly_plan():
    monday_form = SelectRecipe()
    a = db.session.query(Recipe.name).order_by(Recipe.name)
    a = [i[0] for i in a]
    monday_form.name.choices = [("")] + [(x) for x in a]
    tuesday_form = SelectRecipe()
    tuesday_form.name.choices = [("")] + [(x) for x in a]
    wednesday_form = SelectRecipe()
    wednesday_form.name.choices = [("")] + [(x) for x in a]
    thursday_form = SelectRecipe()
    thursday_form.name.choices = [("")] + [(x) for x in a]
    friday_form = SelectRecipe()
    friday_form.name.choices = [("")] + [(x) for x in a]
    saturday_form = SelectRecipe()
    saturday_form.name.choices = [("")] + [(x) for x in a]
    sunday_form = SelectRecipe()
    sunday_form.name.choices = [("")] + [(x) for x in a]
    if monday_form.validate_on_submit():
        return render_template(
            "weekly_planner.html",
            monday_form=monday_form,
            tuesday_form=tuesday_form,
            wednesday_form=wednesday_form,
            thursday_form=thursday_form,
            friday_form=friday_form,
            saturday_form=saturday_form,
            sunday_form=sunday_form,
            a=a,
        )
    return render_template(
        "weekly_planner.html",
        monday_form=monday_form,
        tuesday_form=tuesday_form,
        wednesday_form=wednesday_form,
        thursday_form=thursday_form,
        friday_form=friday_form,
        saturday_form=saturday_form,
        sunday_form=sunday_form,
        a=a,
    )


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
    # our_add = Shopping.query.order_by(Shopping.aisle_id)
    deleted_items = (
        Dshopping.query.with_entities(
            Dshopping.ingredient_name,
            Dshopping.qty,
            Dshopping.unit_name,
            Dshopping.aisle_name,
            Dshopping.aisle_id,
            func.sum(Dshopping.qty).label("dtotal"),
        )
        .group_by(Dshopping.ingredient_name)
        .order_by(Dshopping.ingredient_name)
        .all()
    )
    our_add = (
        Shopping.query.with_entities(
            Shopping.ingredient_name,
            Shopping.qty,
            Shopping.unit_name,
            Shopping.aisle_name,
            Shopping.aisle_id,
            func.sum(Shopping.qty).label("total"),
        )
        .group_by(Shopping.ingredient_name)
        .order_by(Shopping.ingredient_name)
        .all()
    )
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
        our_add = (
            Shopping.query.with_entities(
                Shopping.ingredient_name,
                Shopping.qty,
                Shopping.unit_name,
                Shopping.aisle_name,
                Shopping.aisle_id,
                func.sum(Shopping.qty).label("total"),
            )
            .group_by(Shopping.ingredient_name)
            .order_by(Shopping.ingredient_name)
            .all()
        )
        deleted_items = (
            Dshopping.query.with_entities(
                Dshopping.ingredient_name,
                Dshopping.qty,
                Dshopping.unit_name,
                Dshopping.aisle_name,
                Dshopping.aisle_id,
                func.sum(Dshopping.qty).label("dtotal"),
            )
            .group_by(Dshopping.ingredient_name)
            .order_by(Dshopping.ingredient_name)
            .all()
        )
        return render_template(
            "list.html",
            form=form,
            form2=form2,
            item=item,
            name=name,
            our_add=our_add,
            deleted_items=deleted_items,
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
        our_add = (
            Shopping.query.with_entities(
                Shopping.ingredient_name,
                Shopping.qty,
                Shopping.unit_name,
                Shopping.aisle_name,
                Shopping.aisle_id,
                func.sum(Shopping.qty).label("total"),
            )
            .group_by(Shopping.ingredient_name)
            .order_by(Shopping.ingredient_name)
            .all()
        )
        deleted_items = (
            Dshopping.query.with_entities(
                Dshopping.ingredient_name,
                Dshopping.qty,
                Dshopping.unit_name,
                Dshopping.aisle_name,
                Dshopping.aisle_id,
                func.sum(Dshopping.qty).label("dtotal"),
            )
            .group_by(Dshopping.ingredient_name)
            .order_by(Dshopping.ingredient_name)
            .all()
        )
        form2.item.data = ""
        return render_template(
            "list.html",
            form=form,
            form2=form2,
            item=item,
            name=name,
            our_add=our_add,
            deleted_items=deleted_items,
        )
    else:
        return render_template(
            "list.html",
            form=form,
            form2=form2,
            item=item,
            name=name,
            our_add=our_add,
            deleted_items=deleted_items,
        )


@app.route("/list/delete/<ingredient_name>")
def delete_shopping_item(ingredient_name):
    q = Shopping.query.filter_by(ingredient_name=ingredient_name).first()
    our_add = (
        Shopping.query.with_entities(
            Shopping.ingredient_name,
            Shopping.qty,
            Shopping.unit_name,
            Shopping.aisle_name,
            Shopping.aisle_id,
            func.sum(Shopping.qty).label("total"),
        )
        .group_by(Shopping.ingredient_name)
        .order_by(Shopping.ingredient_name)
        .all()
    )
    deleted_items = (
        Dshopping.query.with_entities(
            Dshopping.ingredient_name,
            Dshopping.qty,
            Dshopping.unit_name,
            Dshopping.aisle_name,
            Dshopping.aisle_id,
            func.sum(Dshopping.qty).label("dtotal"),
        )
        .group_by(Dshopping.ingredient_name)
        .order_by(Dshopping.ingredient_name)
        .all()
    )
    try:
        while q.id > 0:
            update = Dshopping(
                ingredient_name=q.ingredient_name,
                qty=q.qty,
                unit_name=q.unit_name,
                aisle_name=q.aisle_name,
                aisle_id=q.aisle_id,
            )
            db.session.add(update)
            db.session.delete(q)
            db.session.commit()
            q = Shopping.query.filter_by(ingredient_name=ingredient_name).first()
            our_add = (
                Shopping.query.with_entities(
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.ingredient_name)
                .all()
            )
            deleted_items = (
                Dshopping.query.with_entities(
                    Dshopping.ingredient_name,
                    Dshopping.qty,
                    Dshopping.unit_name,
                    Dshopping.aisle_name,
                    Dshopping.aisle_id,
                    func.sum(Dshopping.qty).label("dtotal"),
                )
                .group_by(Dshopping.ingredient_name)
                .order_by(Dshopping.ingredient_name)
                .all()
            )
        else:
            return render_template(
                "list_delete.html", our_add=our_add, deleted_items=deleted_items
            )
    except:
        return render_template(
            "list_delete.html", our_add=our_add, deleted_items=deleted_items
        )


####################
# INGREDIENTS LIST #
####################
"""Add Ingredient"""


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


"""Update Ingredient"""


@app.route("/ingredients/<int:id>", methods=["GET", "POST"])
def ingredient_edit(id):
    editing_item = Ingredient.query.get(id)
    form = CreateIngredient()
    x = db.session.query(Unit.label).order_by(Unit.label)
    x = [i[0] for i in x]
    form.unit.choices = [("")] + [(y) for y in x]
    a = db.session.query(Aisle.name).order_by(Aisle.name)
    a = [i[0] for i in a]
    form.aisle.choices = [("")] + [(b) for b in a]
    ingredient_to_update = Ingredient.query.get_or_404(id)
    if form.validate_on_submit():
        uid = Unit.query.filter_by(label=form.unit.data).first()
        aid = Aisle.query.filter_by(name=form.aisle.data).first()
        ingredient_to_update.name = form.name.data
        ingredient_to_update.unit_id = uid.id
        ingredient_to_update.aisle_id = aid.id
        db.session.commit()
    return render_template(
        "ingredient_update.html",
        ingredient_to_update=ingredient_to_update,
        form=form,
        editing_item=editing_item,
    )
