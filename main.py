from itertools import groupby
from pickle import NONE
from tkinter.tix import Select
from unicodedata import name
from flask import Flask, flash, render_template, request
from models import (
    Ingredient,
    Aisle,
    Shopping,
    Dshopping,
    Recipe,
    RecipeIngredient,
    Unit,
    Weekly_Recipe,
    connect_db,
    db,
)
from forms import (
    ManualShoppingForm,
    ShoppingForm,
    CreateIngredient,
    SelectRecipe,
    SelectRecipe2,
    SelectRecipe3,
    SelectRecipe4,
    SelectRecipe5,
    SelectRecipe6,
    SelectRecipe7,
)
from sqlalchemy import func
from decimal import Decimal


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
@app.route("/weekly_plan", methods=["GET", "POST"])
def weekly_plan():
    monday_form = SelectRecipe()
    monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
    a = db.session.query(Recipe.name).order_by(Recipe.name)
    a = [i[0] for i in a]
    monday_form.name.choices = [("")] + [(x) for x in a]
    tuesday_form = SelectRecipe2()
    tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
    tuesday_form.name2.choices = [("")] + [(x) for x in a]
    wednesday_form = SelectRecipe3()
    wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
    wednesday_form.name3.choices = [("")] + [(x) for x in a]
    thursday_form = SelectRecipe4()
    thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
    thursday_form.name4.choices = [("")] + [(x) for x in a]
    friday_form = SelectRecipe5()
    friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
    friday_form.name5.choices = [("")] + [(x) for x in a]
    saturday_form = SelectRecipe6()
    saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
    saturday_form.name6.choices = [("")] + [(x) for x in a]
    sunday_form = SelectRecipe7()
    sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
    sunday_form.name7.choices = [("")] + [(x) for x in a]
    if monday_form.submit.data and monday_form.validate_on_submit():
        u_mon1 = Recipe.query.filter_by(name=monday_form.name.data).first()
        u_mon2 = (
            RecipeIngredient.query.filter_by(rid=u_mon1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_mon2:
            u_mon4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=monday_form.rqty.data * Decimal(x.qty),
                unit_name=x.ingredient.unit.label,
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="monday",
            )
            db.session.add(u_mon4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(1)
            weekly.rname = monday_form.name.data
            db.session.commit()
            monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
            tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
            wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
            thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
            friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
            saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
            sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
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
            x=x,
        )
    if tuesday_form.submit2.data and tuesday_form.validate_on_submit():
        u_tue1 = Recipe.query.filter_by(name=tuesday_form.name2.data).first()
        u_tue2 = (
            RecipeIngredient.query.filter_by(rid=u_tue1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_tue2:
            u_tue4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=tuesday_form.rqty2.data * Decimal(x.qty),
                unit_name=x.ingredient.unit.label,
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="tuesday",
            )
            db.session.add(u_tue4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(2)
            weekly.rname = tuesday_form.name2.data
            db.session.commit()
            monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
            tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
            wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
            thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
            friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
            saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
            sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
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
            x=x,
        )
    if wednesday_form.submit3.data and wednesday_form.validate_on_submit():
        u_wed1 = Recipe.query.filter_by(name=wednesday_form.name3.data).first()
        u_wed2 = (
            RecipeIngredient.query.filter_by(rid=u_wed1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_wed2:
            u_wed4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=wednesday_form.rqty3.data * Decimal(x.qty),
                unit_name=x.ingredient.unit.label,
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="wednesday",
            )
            db.session.add(u_wed4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(3)
            weekly.rname = wednesday_form.name3.data
            db.session.commit()
            monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
            tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
            wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
            thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
            friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
            saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
            sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
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
            x=x,
        )
    if thursday_form.submit4.data and thursday_form.validate_on_submit():
        u_thur1 = Recipe.query.filter_by(name=thursday_form.name4.data).first()
        u_thur2 = (
            RecipeIngredient.query.filter_by(rid=u_thur1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_thur2:
            u_thur4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=thursday_form.rqty4.data * Decimal(x.qty),
                unit_name=x.ingredient.unit.label,
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="thursday",
            )
            db.session.add(u_thur4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(4)
            weekly.rname = thursday_form.name4.data
            db.session.commit()
            monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
            tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
            wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
            thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
            friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
            saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
            sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
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
            x=x,
        )
    if friday_form.submit5.data and friday_form.validate_on_submit():
        u_fri1 = Recipe.query.filter_by(name=friday_form.name5.data).first()
        u_fri2 = (
            RecipeIngredient.query.filter_by(rid=u_fri1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_fri2:
            u_fri4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=friday_form.rqty5.data * Decimal(x.qty),
                unit_name=x.ingredient.unit.label,
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="friday",
            )
            db.session.add(u_fri4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(5)
            weekly.rname = friday_form.name5.data
            db.session.commit()
            monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
            tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
            wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
            thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
            friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
            saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
            sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
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
            x=x,
        )
    if saturday_form.submit6.data and saturday_form.validate_on_submit():
        u_sat1 = Recipe.query.filter_by(name=saturday_form.name6.data).first()
        u_sat2 = (
            RecipeIngredient.query.filter_by(rid=u_sat1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_sat2:
            u_sat4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=saturday_form.rqty6.data * Decimal(x.qty),
                unit_name=x.ingredient.unit.label,
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="saturday",
            )
            db.session.add(u_sat4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(6)
            weekly.rname = saturday_form.name6.data
            db.session.commit()
            monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
            tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
            wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
            thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
            friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
            saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
            sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
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
            x=x,
        )
    if sunday_form.submit7.data and sunday_form.validate_on_submit():
        u_sun1 = Recipe.query.filter_by(name=sunday_form.name7.data).first()
        u_sun2 = (
            RecipeIngredient.query.filter_by(rid=u_sun1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_sun2:
            u_sun4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=sunday_form.rqty7.data * Decimal(x.qty),
                unit_name=x.ingredient.unit.label,
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="saturday",
            )
            db.session.add(u_sun4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(7)
            weekly.rname = sunday_form.name7.data
            db.session.commit()
            monday_form.name.label.text = Weekly_Recipe.query.get(1).rname
            tuesday_form.name2.label.text = Weekly_Recipe.query.get(2).rname
            wednesday_form.name3.label.text = Weekly_Recipe.query.get(3).rname
            thursday_form.name4.label.text = Weekly_Recipe.query.get(4).rname
            friday_form.name5.label.text = Weekly_Recipe.query.get(5).rname
            saturday_form.name6.label.text = Weekly_Recipe.query.get(6).rname
            sunday_form.name7.label.text = Weekly_Recipe.query.get(7).rname
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
            x=x,
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
        .order_by(Dshopping.id.desc())
        .limit(100)
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
            .order_by(Dshopping.id.desc())
            .limit(100)
            .all()
        )
        return render_template(
            "list.html",
            form=form,
            form2=form2,
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
            .order_by(Dshopping.id.desc())
            .limit(100)
            .all()
        )
        return render_template(
            "list.html",
            form=form,
            form2=form2,
            name=name,
            our_add=our_add,
            deleted_items=deleted_items,
        )
    else:
        return render_template(
            "list.html",
            form=form,
            form2=form2,
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
        .order_by(Dshopping.id.desc())
        .limit(100)
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
                .order_by(Dshopping.id.desc())
                .limit(100)
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


@app.route("/list/delete_all")
def delete_all_checked_items():
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
        .order_by(Dshopping.id.desc())
        .limit(100)
        .all()
    )
    try:
        db.session.query(Dshopping).delete()
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
            .order_by(Dshopping.id.desc())
            .limit(100)
            .all()
        )
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
