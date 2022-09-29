from itertools import groupby
from re import U
from tkinter.tix import Select
from unicodedata import name
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from models import (
    Ingredient,
    Aisle,
    Shopping,
    Dshopping,
    Recipe,
    RecipeIngredient,
    RecipeInstruction,
    Unit,
    UnitIngredient,
    Weekly_Recipe,
    RecipeMultiplyer,
    connect_db,
    db,
)
from forms import (
    ManualShoppingForm,
    SelectColor,
    ShoppingForm,
    CreateIngredient,
    CreateRecipe,
    AddIngredient,
    AddInstruction,
    SelectRecipe,
    SelectRecipe2,
    SelectRecipe3,
    SelectRecipe4,
    SelectRecipe5,
    SelectRecipe6,
    SelectRecipe7,
    AddUnitConversion,
    AddUnit,
    RecipeMulti,
    SelectField,
)
from sqlalchemy import func
from decimal import Decimal
import logging
from flask_migrate import Migrate


app = Flask(__name__)


app.config["SECRET_KEY"] = "sk"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food.db"

connect_db(app)
migrate = Migrate(app, db)

handler = logging.FileHandler("test.log")  # Create the file logger
app.logger.addHandler(handler)  # Add it to the built-in logger
app.logger.setLevel(logging.DEBUG)  # Set the log level to debug


@app.route("/")
def index():
    return render_template("index.html")


@app.template_filter()
def color_label(my_var):
    td_class = ""
    if my_var == "blue":
        td_class = "table-blue"
    elif my_var == "dark grey":
        td_class = "table-dark-grey"
    elif my_var == "green":
        td_class = "table-green"
    elif my_var == "light blue":
        td_class = "table-light-blue"
    elif my_var == "yellow":
        td_class = "table-yellow"
    elif my_var == "red":
        td_class = "table-red"
    elif my_var == "light grey":
        td_class = "table-light-grey"
    elif my_var == "purple":
        td_class = "table-purple"
    elif my_var == "orange":
        td_class = "table-orange"
    return td_class

#################
## Weekly VIEW ##
#################
@app.route("/weekly_view", methods=["GET", "POST"])
def weekly_view():
    monday_ingredients = (
                Shopping.query.filter_by(day_label = "monday").with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    Shopping.day_label,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
                .all()
            )
    tuesday_ingredients = (
                Shopping.query.filter_by(day_label = "tuesday").with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    Shopping.day_label,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
                .all()
            )
    wednesday_ingredients = (
                Shopping.query.filter_by(day_label = "wednesday").with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    Shopping.day_label,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
                .all()
            )
    thrusday_ingredients = (
                Shopping.query.filter_by(day_label = "thursday").with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    Shopping.day_label,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
                .all()
            )
    firday_ingredients = (
                Shopping.query.filter_by(day_label = "friday").with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    Shopping.day_label,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
                .all()
            )
    saturday_ingredients = (
                Shopping.query.filter_by(day_label = "saturday").with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    Shopping.day_label,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
                .all()
            )
    sunday_ingredients = (
                Shopping.query.filter_by(day_label = "sunday").with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    Shopping.day_label,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
                .all()
            )
    return render_template("/weekly_view.html", monday_ingredients=monday_ingredients, tuesday_ingredients=tuesday_ingredients, wednesday_ingredients=wednesday_ingredients, thrusday_ingredients=thrusday_ingredients, firday_ingredients=firday_ingredients, saturday_ingredients=saturday_ingredients, sunday_ingredients=sunday_ingredients)

#################
## Weekly Plan ##
#################
@app.route("/weekly_plan", methods=["GET", "POST"])
def weekly_plan():
    monday_form = SelectRecipe()
    a = db.session.query(Recipe.name).order_by(Recipe.name)
    a = [i[0] for i in a]
    monday_form.name.choices = [("")] + [(x) for x in a]
    tuesday_form = SelectRecipe()
    tuesday_form.name.choices = [("")] + [(x) for x in a]
    wednesday_form = SelectRecipe3()
    wednesday_form.name3.choices = [("")] + [(x) for x in a]
    thursday_form = SelectRecipe4()
    thursday_form.name4.choices = [("")] + [(x) for x in a]
    friday_form = SelectRecipe5()
    friday_form.name5.choices = [("")] + [(x) for x in a]
    saturday_form = SelectRecipe6()
    saturday_form.name6.choices = [("")] + [(x) for x in a]
    sunday_form = SelectRecipe7()
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
                unit_name=x.ingredient.default_ingredient_unit(),
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
    if tuesday_form.submit.data and tuesday_form.validate_on_submit():
        u_tue1 = Recipe.query.filter_by(name=tuesday_form.name.data).first()
        u_tue2 = (
            RecipeIngredient.query.filter_by(rid=u_tue1.id)
            .order_by(RecipeIngredient.rid)
            .all()
        )
        for x in u_tue2:
            u_tue4 = Shopping(
                ingredient_name=x.ingredient.name,
                qty=tuesday_form.rqty.data * Decimal(x.qty),
                unit_name=x.ingredient.default_ingredient_unit(),
                aisle_name=x.ingredient.aisle.name,
                aisle_id=x.ingredient.aisle_id,
                day_label="tuesday",
            )
            db.session.add(u_tue4)
            db.session.commit()
        else:
            weekly = Weekly_Recipe.query.get_or_404(2)
            weekly.rname = tuesday_form.name.data
            db.session.commit()
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
                unit_name=x.ingredient.default_ingredient_unit(),
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
                unit_name=x.ingredient.default_ingredient_unit(),
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
                unit_name=x.ingredient.default_ingredient_unit(),
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
                unit_name=x.ingredient.default_ingredient_unit(),
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
                unit_name=x.ingredient.default_ingredient_unit(),
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


####################
## RECIPE ADD NEW ##
####################
@app.route("/unit_label_update", methods=["GET", "POST"])
def unit_label_update():
    if request.method == "POST":
        y = request.json
        x = Ingredient.query.filter_by(name=y).first()
        return jsonify(x.default_ingredient_unit())


@app.route("/url_to_flask_view_function", methods=["GET", "POST"])
def form_processing():
    # the value of the first dropdown (selected by the user)
    selected_class = request.args.get("selected_class", type=str)
    # Get Ingredient by Name
    iid = Ingredient.query.filter_by(name=selected_class).first()
    uids = db.session.query(UnitIngredient.name).filter(UnitIngredient.iid == iid.id)
    updated_values = uids
    # get values for the second dropdown
    # updated_values = db.session.query(Ingredient.name).order_by(Ingredient.name)
    updated_values = [i[0] for i in updated_values]
    # create the value sin the dropdown as a html string
    html_string_selected = ""
    for entry in updated_values:
        html_string_selected += '<option value="{}">{}</option>'.format(entry, entry)

    return jsonify(html_string_selected=html_string_selected)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    form = CreateRecipe()
    if form.submit2.data and form.validate_on_submit():
        update = Recipe(
            name=form.recipe_name.data,
            course=form.course.data,
            servings=form.servings.data,
            serving_size=form.serving_size.data,
        )
        db.session.add(update)
        db.session.commit()
        new_entry = Recipe.query.order_by(Recipe.id.desc()).first()
        return redirect(url_for("recipe_edit", id=new_entry.id))
    return render_template("/recipes/add_recipe.html", form=form)


#################
## RECIPE LIST ##
#################
"""View Specific Recipe"""


@app.route("/recipe_list")
def recipe_list():
    recipe_list = Recipe.query.order_by(Recipe.name)
    return render_template("/recipes/recipe_list.html", recipe_list=recipe_list)


#################
## RECIPE EDIT ##
#################

"""Edit Recipe"""


@app.route("/recipe/<int:id>/edit", methods=["GET", "POST"])
def recipe_edit(id):
    """Page Load Info"""
    r = Recipe.query.get_or_404(id)
    title = r.name
    x = 1
    iquery = RecipeIngredient.query.filter_by(rid=id).all()
    """Update Meta Data Form"""
    form2 = CreateRecipe()
    """Add Ingredient Form"""
    form = AddIngredient()
    a = db.session.query(Ingredient.name).order_by(Ingredient.name)
    a = [i[0] for i in a]
    form.name.choices = [("")] + [(y) for y in a]
    b = db.session.query(Unit.name).order_by(Unit.id)
    b = [i[0] for i in b]
    form.unit.choices = [("")] + [(y) for y in b]
    """Add Instruction Step Form"""
    form3 = AddInstruction()
    instruct_query = RecipeInstruction.query.filter_by(rid=id).all()
    """Add Ingredient Button Action"""
    if form.submit.data and form.validate_on_submit():
        u1 = Ingredient.query.filter_by(name=form.name.data).first()
        u2 = Unit.query.filter_by(name=form.unit.data).first()
        u3 = UnitIngredient.query.filter_by(iid=u1.id, uid=u2.id).first()
        update = RecipeIngredient(
            rid=id,
            iid=u1.id,
            qty=form.qty.data * Decimal(u3.multiplyer),
            unit_suffix=form.suffix.data,
        )
        db.session.add(update)
        db.session.commit()
        iquery = RecipeIngredient.query.filter_by(rid=id).all()
        form.name.data = ""
        return render_template(
            "/recipes/recipe_edit.html",
            r=r,
            title=title,
            x=x,
            iquery=iquery,
            form=form,
            form2=form2,
            form3=form3,
            instruct_query=instruct_query,
        )
    """Update Meta Data Button Action"""
    if form2.submit2.data and form2.validate_on_submit():
        r.name = form2.recipe_name.data
        r.course = form2.course.data
        r.servings = form2.servings.data
        r.serving_size = form2.serving_size.data
        db.session.commit()
    """Add Instruction Step Button Action"""
    if form3.submit3.data and form3.validate_on_submit():
        update = RecipeInstruction(rid=id, instruction=form3.instruction.data)
        db.session.add(update)
        db.session.commit()
        instruct_query = RecipeInstruction.query.filter_by(rid=id).all()

    return render_template(
        "/recipes/recipe_edit.html",
        r=r,
        title=r.name,
        x=x,
        iquery=iquery,
        form=form,
        form2=form2,
        form3=form3,
        instruct_query=instruct_query,
    )


"""Move Recipe Ingredient Down in List"""


@app.route("/recipe/<int:rid>/edit/down/<int:id>", methods=["GET", "POST"])
def recipe_ingredient_move_down(rid, id):
    a = RecipeIngredient.query.get_or_404(id)
    b = RecipeIngredient.query.filter(
        RecipeIngredient.rid == rid, RecipeIngredient.id > a.id
    ).first_or_404()

    w = a.iid
    x = a.qty
    y = a.unit_suffix
    z = a.ingredient_color_tag

    a.iid = b.iid
    a.qty = b.qty
    a.unit_suffix = b.unit_suffix
    a.ingredient_color_tag = b.ingredient_color_tag

    b.iid = w
    b.qty = x
    b.unit_suffix = y
    b.ingredient_color_tag = z

    db.session.commit()
    return redirect(url_for("recipe_edit", id=rid))


"""Edit Ingredient Recipe"""


@app.route("/recipes/edit_recipe_ingredient/<int:id>", methods=["GET", "POST"])
def recipe_edit_ingredient(id):
    c = RecipeIngredient.query.get_or_404(id)
    r = Recipe.query.filter_by(id=c.rid).first()
    n = Ingredient.query.filter_by(id=c.iid).first()
    rid = c.rid
    """Add Ingredient Form"""
    form = AddIngredient()
    a = db.session.query(Ingredient.name).order_by(Ingredient.name)
    a = [i[0] for i in a]
    form.name.choices = [("")] + [(y) for y in a]
    b = db.session.query(Unit.name).order_by(Unit.id)
    b = [i[0] for i in b]
    form.unit.choices = [("")] + [(y) for y in b]
    """Color Tag"""
    form2 = SelectColor()
    """Add Ingredient Button Action"""
    if form.submit.data and form.validate_on_submit():
        u1 = Ingredient.query.filter_by(name=form.name.data).first()
        u2 = Unit.query.filter_by(name=form.unit.data).first()
        u3 = UnitIngredient.query.filter_by(iid=u1.id, uid=u2.id).first()
        c.iid = u1.id
        c.qty = form.qty.data * Decimal(u3.multiplyer)
        c.unit_suffix = form.suffix.data
        db.session.commit()
        return render_template(
            "/recipes/edit_recipe_ingredient.html",
            id=rid,
            r=r,
            form=form,
            c=c,
            n=n,
            form2=form2,
        )
    if form2.submit.data and form2.validate_on_submit():
        c.ingredient_color_tag = form2.name.data
        db.session.commit()
    return render_template(
        "/recipes/edit_recipe_ingredient.html",
        id=rid,
        r=r,
        form=form,
        c=c,
        n=n,
        form2=form2,
    )


"""Delete Recipe Ingredient"""


@app.route("/recipes/delete_recipe_ingredient/<int:id>", methods=["GET", "POST"])
def recipe_delete_ingredient(id):
    a = RecipeIngredient.query.get_or_404(id)
    rid = a.rid
    db.session.delete(a)
    db.session.commit()

    return redirect(url_for("recipe_edit", id=rid))


"""Move Recipe Instruction Down in List"""


@app.route("/recipe/<int:rid>/edit_instruction/down/<int:id>", methods=["GET", "POST"])
def recipe_instruction_move_down(rid, id):
    a = RecipeInstruction.query.get_or_404(id)
    b = RecipeInstruction.query.filter(
        RecipeInstruction.rid == rid, RecipeInstruction.id > a.id
    ).first_or_404()

    x = a.instruction
    y = a.instruction_color_tag

    a.instruction = b.instruction
    a.instruction_color_tag = b.instruction_color_tag

    b.instruction = x
    b.instruction_color_tag = y

    db.session.commit()
    return redirect(url_for("recipe_edit", id=rid))


"""Delete Instruction From Recipe"""


@app.route("/recipe/delete_instruction/<int:id>", methods=["GET", "POST"])
def recipe_delete_instruction(id):
    a = RecipeInstruction.query.get_or_404(id)
    rid = a.rid
    db.session.delete(a)
    db.session.commit()

    return redirect(url_for("recipe_edit", id=rid))


"""Edit Instruction From Recipe"""


@app.route("/recipe/edit_instruction/<int:id>", methods=["GET", "POST"])
def recipe_edit_instruction(id):
    a = RecipeInstruction.query.get_or_404(id)
    b = a.instruction
    r = Recipe.query.filter_by(id=a.rid).first()
    """Add Instruction Step Form"""
    form = AddInstruction()
    form2 = SelectColor()
    if request.method == "GET":
        form.instruction.data = b
    if form.submit3.data and form.validate_on_submit():
        form.instruction.data = form.instruction.data
        a.instruction = form.instruction.data
        db.session.commit()
    if form2.submit.data and form2.validate_on_submit():
        a.instruction_color_tag = form2.name.data
        db.session.commit()
    return render_template(
        "/recipes/edit_recipe_instruction.html", a=a, form=form, form2=form2, r=r, b=b
    )


############################
## INDIVIDUAL RECIPE PAGE ##
############################
"""View Specific Recipe"""


@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
    r = Recipe.query.get_or_404(id)
    title = r.name
    iquery = RecipeIngredient.query.filter_by(rid=id).all()
    form = RecipeMulti()
    m = RecipeMultiplyer.query.get_or_404(1)
    instruct_query = RecipeInstruction.query.filter_by(rid=id).all()
    if form.submit.data and form.validate_on_submit():
        m.amount = form.amount.data
        db.session.commit()
    return render_template(
        "/recipes/recipe.html",
        r=r,
        title=title,
        form=form,
        m=m,
        iquery=iquery,
        instruct_query=instruct_query,
    )

"""View Traditional Specific Recipe"""


@app.route("/recipe_traditional/<int:id>", methods=["GET", "POST"])
def recipe_traditional(id):
    r = Recipe.query.get_or_404(id)
    title = r.name
    iquery = RecipeIngredient.query.filter_by(rid=id).all()
    form = RecipeMulti()
    m = RecipeMultiplyer.query.get_or_404(1)
    instruct_query = RecipeInstruction.query.filter_by(rid=id).all()
    if form.submit.data and form.validate_on_submit():
        m.amount = form.amount.data
        db.session.commit()
    return render_template(
        "/recipes/recipe_traditional.html",
        r=r,
        title=title,
        form=form,
        m=m,
        iquery=iquery,
        instruct_query=instruct_query,
    )

###################
## RECIPE DELETE ##
###################

"""Confirmation Page"""


@app.route("/recipe/<int:id>/delete_confirmation")
def delete_recipe_confirmation(id):
    r = Recipe.query.get_or_404(id)
    title = r.name
    return render_template("/recipes/delete_recipe_conf.html", r=r, title=title)


"""Delete Function"""


@app.route(
    "/recipe/<int:id>/delete_confirmation/delete_forever", methods=["GET", "POST"]
)
def recipe_delete_all_ingredient(id):
    recipe = Recipe.query.get_or_404(id)
    ingredients_delete = RecipeIngredient.query.filter_by(rid=id).all()
    instructions_delete = RecipeInstruction.query.filter_by(rid=id).all()
    db.session.delete(recipe)
    for ingredient in ingredients_delete:
        db.session.delete(ingredient)
    for instruction in instructions_delete:
        db.session.delete(instruction)
    db.session.commit()
    return redirect(url_for("recipe_list"))


#################
# SHOPPING LIST #
#################
@app.route("/shopping/list", methods=["GET", "POST"])
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
            Shopping.id,
            Shopping.ingredient_name,
            Shopping.qty,
            Shopping.unit_name,
            Shopping.aisle_name,
            Shopping.aisle_id,
            func.sum(Shopping.qty).label("total"),
        )
        .group_by(Shopping.ingredient_name)
        .order_by(Shopping.aisle_id)
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
            unit_name=u1.default_ingredient_unit(),
            aisle_name=u1.aisle.name,
            aisle_id=u1.aisle_id,
        )
        db.session.add(update)
        db.session.commit()
        our_add = (
            Shopping.query.with_entities(
                Shopping.id,
                Shopping.ingredient_name,
                Shopping.qty,
                Shopping.unit_name,
                Shopping.aisle_name,
                Shopping.aisle_id,
                func.sum(Shopping.qty).label("total"),
            )
            .group_by(Shopping.ingredient_name)
            .order_by(Shopping.aisle_id)
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
            "shopping/list.html",
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
                Shopping.id,
                Shopping.ingredient_name,
                Shopping.qty,
                Shopping.unit_name,
                Shopping.aisle_name,
                Shopping.aisle_id,
                func.sum(Shopping.qty).label("total"),
            )
            .group_by(Shopping.ingredient_name)
            .order_by(Shopping.aisle_id)
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
            "shopping/list.html",
            form=form,
            form2=form2,
            name=name,
            our_add=our_add,
            deleted_items=deleted_items,
        )
    else:
        return render_template(
            "shopping/list.html",
            form=form,
            form2=form2,
            name=name,
            our_add=our_add,
            deleted_items=deleted_items,
        )


@app.route("/shopping/list/delete/<int:id>")
def delete_shopping_item(id):
    get_name = Shopping.query.get_or_404(id)
    q = Shopping.query.filter_by(ingredient_name=get_name.ingredient_name).first()
    our_add = (
        Shopping.query.with_entities(
            Shopping.id,
            Shopping.ingredient_name,
            Shopping.qty,
            Shopping.unit_name,
            Shopping.aisle_name,
            Shopping.aisle_id,
            func.sum(Shopping.qty).label("total"),
        )
        .group_by(Shopping.ingredient_name)
        .order_by(Shopping.aisle_id)
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
            q = Shopping.query.filter_by(
                ingredient_name=get_name.ingredient_name
            ).first()
            our_add = (
                Shopping.query.with_entities(
                    Shopping.id,
                    Shopping.ingredient_name,
                    Shopping.qty,
                    Shopping.unit_name,
                    Shopping.aisle_name,
                    Shopping.aisle_id,
                    func.sum(Shopping.qty).label("total"),
                )
                .group_by(Shopping.ingredient_name)
                .order_by(Shopping.aisle_id)
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
                "shopping/list_delete.html", our_add=our_add, deleted_items=deleted_items
            )
    except:
        return render_template(
            "shopping/list_delete.html", our_add=our_add, deleted_items=deleted_items
        )


@app.route("/shopping/list/delete_all")
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
            "shopping/list_delete.html", our_add=our_add, deleted_items=deleted_items
        )
    except:
        return render_template(
            "shopping/list_delete.html", our_add=our_add, deleted_items=deleted_items
        )


####################
# INGREDIENTS LIST #
####################
"""Add Ingredient"""


@app.route("/ingredients/ingredients", methods=["GET", "POST"])
def ingredient_page():
    ingredient_list = Ingredient.query.order_by(func.lower(Ingredient.name))
    x = db.session.query(Unit.name).order_by(Unit.oid)
    x = [i[0] for i in x]
    form = CreateIngredient()
    form.unit.choices = [("")] + [(y) for y in x]
    a = db.session.query(Aisle.name).order_by(Aisle.id)
    a = [i[0] for i in a]
    form.aisle.choices = [("")] + [(b) for b in a]
    if form.validate_on_submit():
        uid = Unit.query.filter_by(name=form.unit.data).first()
        aid = Aisle.query.filter_by(name=form.aisle.data).first()
        cal = (form.protein.data * 4) + (form.carbs.data * 4) + (form.fat.data * 9)
        u_price = (form.item_price.data) / (form.item_unit_size.data)
        update = Ingredient(
            name=form.name.data,
            icalories=cal,
            protein=form.protein.data,
            carbs=form.carbs.data,
            fat=form.fat.data,
            fiber=form.fiber.data,
            sugar=form.sugar.data,
            item_unit_size=form.item_unit_size.data,
            item_price=form.item_price.data,
            u_price=u_price,
            aisle_id=aid.id,
        )
        db.session.add(update)
        db.session.commit()
        iid = Ingredient.query.order_by(Ingredient.id.desc()).first()
        update2 = UnitIngredient(uid=uid.id, iid=iid.id, name=uid.name, multiplyer=1)
        db.session.add(update2)
        db.session.commit()
    return render_template(
        "/ingredients/ingredients.html",
        x=x,
        a=a,
        form=form,
        ingredient_list=ingredient_list,
    )


"""Update Ingredient"""


@app.route("/ingredients/ingredients/<int:id>", methods=["GET", "POST"])
def ingredient_edit(id):
    """Ingredient Meta Edit"""
    editing_item = Ingredient.query.get(id)
    units = UnitIngredient.query.filter_by(iid=id).all()
    form = CreateIngredient()
    x = db.session.query(Unit.name).order_by(Unit.oid)
    x = [i[0] for i in x]
    form.unit.choices = [("")] + [(y) for y in x]
    a = db.session.query(Aisle.name).order_by(Aisle.id)
    a = [i[0] for i in a]
    form.aisle.choices = [("")] + [(b) for b in a]
    ingredient_to_update = Ingredient.query.get_or_404(id)
    unit_to_update = UnitIngredient.query.filter_by(iid=id).first()
    """Add Conversion Option"""
    form2 = AddUnitConversion()
    form2.unit2.choices = [("")] + [(y) for y in x]
    if form.submit.data and form.validate_on_submit():
        uid = Unit.query.filter_by(name=form.unit.data).first()
        aid = Aisle.query.filter_by(name=form.aisle.data).first()
        cal = (form.protein.data * 4) + (form.carbs.data * 4) + (form.fat.data * 9)
        u_price = (form.item_price.data) / (form.item_unit_size.data)
        ingredient_to_update.name = form.name.data
        ingredient_to_update.icalories = cal
        ingredient_to_update.protein = form.protein.data
        ingredient_to_update.carbs = form.carbs.data
        ingredient_to_update.fat = form.fat.data
        ingredient_to_update.fiber = form.fiber.data
        ingredient_to_update.sugar = form.sugar.data
        ingredient_to_update.item_unit_size = form.item_unit_size.data
        ingredient_to_update.item_price = form.item_price.data
        ingredient_to_update.u_price = u_price
        ingredient_to_update.aisle_id = aid.id
        unit_to_update.uid = uid.id
        unit_to_update.name = uid.name
        db.session.commit()
    if form2.submit2.data and form2.validate_on_submit():
        uid = Unit.query.filter_by(name=form2.unit2.data).first()
        update2 = UnitIngredient(
            iid=id, uid=uid.id, name=uid.name, multiplyer=form2.multiplyer.data
        )
        db.session.add(update2)
        db.session.commit()
        units = UnitIngredient.query.filter_by(iid=id).all()
    else:
        print("noo luck")
    return render_template(
        "/ingredients/ingredient_update.html",
        ingredient_to_update=ingredient_to_update,
        form=form,
        editing_item=editing_item,
        form2=form2,
        units=units,
    )


"""Delete Ingredient From Database Confirmatioin Page"""


@app.route("/ingredients/ingredient/<int:id>/delete_confirmation")
def delete_ingredient_confirmation(id):
    r = Ingredient.query.get_or_404(id)
    title = r.name
    return render_template("/ingredients/ingredient_recipe_conf.html", r=r, title=title)


""""Delete Ingredient From Database Function"""


@app.route(
    "/ingredients/ingredient/<int:id>/delete_confirmation/delete_forever",
    methods=["GET", "POST"],
)
def ingredient_delete(id):
    ingredient = Ingredient.query.get_or_404(id)
    recipe_ingredients = RecipeIngredient.query.filter_by(iid=id).all()
    unit_ingredients = UnitIngredient.query.filter_by(iid=id).all()
    for unit_ingredient in unit_ingredients:
        db.session.delete(unit_ingredient)
    for recipe_ingredient in recipe_ingredients:
        db.session.delete(recipe_ingredient)
    db.session.delete(ingredient)
    db.session.commit()
    return redirect(url_for("ingredient_page"))


"""Unit Conversion Update"""


@app.route("/unit_conversion_update/<int:id>", methods=["GET", "POST"])
def unit_conversion_update(id):
    unit_to_update = UnitIngredient.query.get(id)
    title = Ingredient.query.get(unit_to_update.iid)
    form = AddUnitConversion()
    x = db.session.query(Unit.name).order_by(Unit.oid)
    x = [i[0] for i in x]
    form.unit2.choices = [("")] + [(y) for y in x]
    if form.submit2.data and form.validate_on_submit():
        uid = Unit.query.filter_by(name=form.unit2.data).first()
        unit_to_update.uid = uid.id
        unit_to_update.name = uid.name
        unit_to_update.multiplyer = form.multiplyer.data
        db.session.commit()
        return redirect(url_for("ingredient_edit", id=unit_to_update.iid))
    return render_template(
        "/units/unit_conversion_update.html",
        form=form,
        unit_to_update=unit_to_update,
        title=title,
    )


"""Delete Unit Conversion"""


@app.route("/unit_conversion_delete/<int:id>", methods=["GET", "POST"])
def unit_conversion_delete(id):
    unit_to_update = UnitIngredient.query.get(id)
    db.session.delete(unit_to_update)
    db.session.commit()
    return redirect(url_for("ingredient_edit", id=unit_to_update.iid))


################
# UNIT EDITING #
################

"""Add Unit"""


@app.route("/units", methods=["GET", "POST"])
def unit_page():
    unit_list = Unit.query.order_by(Unit.oid)
    last_oid = Unit.query.order_by(Unit.oid.desc()).first()
    new_oid = last_oid.oid + 1
    form = AddUnit()
    if form.submit.data and form.validate_on_submit():
        update = Unit(oid=new_oid, name=form.unit.data)
        db.session.add(update)
        db.session.commit()
        unit_list = Unit.query.order_by(Unit.oid)
    return render_template("/units/units.html", unit_list=unit_list, form=form)


"""Delete Unit"""


@app.route("/unit/delete/<int:id>", methods=["GET", "POST"])
def unit_delete(id):
    unit_to_update = Unit.query.get(id)
    count = UnitIngredient.query.filter_by(uid=id).count()
    unit_list_to_update = UnitIngredient.query.filter_by(uid=id).all()
    if count == 0:
        db.session.delete(unit_to_update)
        for unit_list in unit_list_to_update:
            db.session.delete(unit_list)
        db.session.commit()
        return redirect(url_for("unit_page"))
    else:
        flash(
            "Cannot delete, unit is within Ingredent. Check default units and conversions. Remove there before deleting the unit."
        )
    return redirect(url_for("unit_page"))


"""Move Unit Order Down"""


@app.route("/unit/edit/down/<int:id>", methods=["GET", "POST"])
def unit_order_move_down(id):
    a = Unit.query.get_or_404(id)
    b = Unit.query.order_by(Unit.oid).filter(Unit.oid > a.oid).first_or_404()

    w = a.oid
    a.oid = b.oid
    b.oid = w

    db.session.commit()
    return redirect(url_for("unit_page"))
