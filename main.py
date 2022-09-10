from pickle import NONE
from unicodedata import name
from flask import Flask, render_template
from models import Ingredient, Aisle, Shopping, connect_db, db
from forms import ShoppingForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "sk"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food.db"

connect_db(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list", methods=["GET", "POST"])
def list():
    item = None
    name = db.session.query(Ingredient.name).order_by(Ingredient.name)
    name = [i[0] for i in name]
    form = ShoppingForm()
    form.name.choices = name
    if form.validate_on_submit():
        try:
            u1 = Ingredient.query.filter_by(name=form.name.data).first()
            update = Shopping(
                ingredient_name=u1.name, aisle_name=u1.aisle.name, aisle_id=u1.aisle_id
            )
            db.session.add(update)
            db.session.commit()
            our_add = Shopping.query.order_by(Shopping.aisle_id)
            return render_template(
                "list.html", form=form, item=item, name=name, our_add=our_add
            )
        except:
            update = Shopping(
                ingredient_name=form.item.data, aisle_name="Unknown", aisle_id=0
            )
            our_add = Shopping.query.order_by(Shopping.aisle_id)
            db.session.add(update)
            db.session.commit()
            return render_template(
                "list.html", form=form, item=item, name=name, our_add=our_add
            )
    else:
        return render_template("list.html", form=form, item=item, name=name)


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
