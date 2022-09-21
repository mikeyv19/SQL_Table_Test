from models import (
    Ingredient,
    Aisle,
    Shopping,
    Unit,
    Recipe,
    RecipeIngredient,
    connect_db,
    Weekly_Recipe,
    db,
)
from main import app

db.drop_all()
db.create_all()

# aisle1 = Aisle(id=1, name="Produce")
# aisle2 = Aisle(id=2, name="Seafood")
# aisle3 = Aisle(id=3, name="7")
# aisle4 = Aisle(id=4, name="14")
# aisle5 = Aisle(id=5, name="Dairy")

# unit1 = Unit(id=1, label="Oz")
# unit2 = Unit(id=2, label="g")
# unit3 = Unit(id=3, label="Egg(s)")
# unit4 = Unit(id=4, label="Fruit(s)")
# unit5 = Unit(id=5, label="Slice(s)")

# ingredient1 = Ingredient(
#     id=1,
#     name="Salt",
#     unit_id=2,
#     icalories=0,
#     protein=0,
#     carbs=0,
#     fat=0,
#     fiber=0,
#     sugar=0,
#     item_unit_size=2270,
#     item_price=15.80,
#     u_price=15.80 / 2270,
#     aisle_id=3,
# )

# ingredient2 = Ingredient(
#     id=2,
#     name="Apple",
#     unit_id=4,
#     icalories=104.7,
#     protein=0.5,
#     carbs=25,
#     fat=0.3,
#     fiber=4.4,
#     sugar=18.9,
#     item_unit_size=1,
#     item_price=1.25,
#     u_price=1.25 / 1,
#     aisle_id=1,
# )
# ingredient3 = Ingredient(
#     id=3,
#     name="Eggs",
#     unit_id=3,
#     icalories=60,
#     protein=6,
#     carbs=0,
#     fat=4,
#     fiber=0,
#     sugar=0,
#     item_unit_size=18,
#     item_price=5.49,
#     u_price=5.49 / 18,
#     aisle_id=5,
# )
# ingredient4 = Ingredient(
#     id=4,
#     name="Salmon",
#     unit_id=1,
#     icalories=46,
#     protein=7,
#     carbs=0,
#     fat=2,
#     fiber=0,
#     sugar=0,
#     item_unit_size=1,
#     item_price=0.687,
#     u_price=0.687 / 1,
#     aisle_id=2,
# )
# ingredient5 = Ingredient(
#     id=5,
#     name="Bread",
#     unit_id=5,
#     icalories=67.2,
#     protein=2,
#     carbs=13,
#     fat=0.8,
#     fiber=0.5,
#     sugar=1.5,
#     item_unit_size=20,
#     item_price=1.29,
#     u_price=1.29 / 20,
#     aisle_id=4,
# )

# db.session.add_all([aisle1, aisle2, aisle3, aisle4, aisle5])
# # db.session.add_all([unit1, unit2, unit3, unit4, unit5])
# # db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5])

# db.session.commit()

# r1 = Recipe(id=1, name="Salty Salmon")
# r2 = Recipe(id=2, name="Eggs and Toast with Fruit")

# db.session.add_all([r1, r2])
# db.session.commit()

# ri1 = RecipeIngredient(id=1, rid=1, iid=1, qty=2.5, unit_suffix="")
# ri3 = RecipeIngredient(id=2, rid=2, iid=2, qty=1, unit_suffix="")
# ri2 = RecipeIngredient(id=3, rid=1, iid=4, qty=48, unit_suffix="Cut in half")
# ri4 = RecipeIngredient(id=4, rid=2, iid=3, qty=2, unit_suffix="")
# ri5 = RecipeIngredient(id=5, rid=2, iid=5, qty=2, unit_suffix="Toasted")
# ri6 = RecipeIngredient(id=6, rid=2, iid=5, qty=1, unit_suffix="Toasted")

# db.session.add_all([ri1, ri2, ri3, ri4, ri5, ri6])
# db.session.commit()

# w1 = Weekly_Recipe(id=1, rname="Recipe")
# w2 = Weekly_Recipe(id=2, rname="Recipe")
# w3 = Weekly_Recipe(id=3, rname="Recipe")
# w4 = Weekly_Recipe(id=4, rname="Recipe")
# w5 = Weekly_Recipe(id=5, rname="Recipe")
# w6 = Weekly_Recipe(id=6, rname="Recipe")
# w7 = Weekly_Recipe(id=7, rname="Recipe")

# db.session.add_all([w1, w2, w3, w4, w5, w6, w7])
# db.session.commit()
