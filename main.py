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
    aisle = None
    form = ShoppingForm()
    if form.validate_on_submit():
        update = Shopping(
            item=form.item.data, aisle=Ingredient.query.filter_by(name=item).first()
        )
        db.session.add(update)
        db.session.commit()
    our_add = Shopping.query.order_by(Shopping.aisle)
    return render_template(
        "list.html", item=item, aisle=aisle, form=form, our_add=our_add
    )


#    our_list = Ingredient.query.order_by(Ingredient.aisle_id)

# food = Ingredient.query.get(1)
# food = ingredient

# class Foods:
#     first_ingredient = Ingredient.query.get(1)
#     first_ingredient_aisle = Ingredient.query.get(1)
#     print(first_ingredient)
#     print(first_ingredient_aisle.aisle.name)
