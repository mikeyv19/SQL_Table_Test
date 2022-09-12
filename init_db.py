from models import Ingredient, Aisle, Shopping, Unit, connect_db, db
from main import app

db.drop_all()
db.create_all()

aisle1 = Aisle(id=1, name="Produce")
aisle2 = Aisle(id=2, name="Seafood")
aisle3 = Aisle(id=3, name="7")
aisle4 = Aisle(id=4, name="14")
aisle5 = Aisle(id=5, name="Dairy")

unit1 = Unit(id=1, label="Oz")
unit2 = Unit(id=2, label="g")
unit3 = Unit(id=3, label="Egg(s)")
unit4 = Unit(id=4, label="Fruit(s)")
unit5 = Unit(id=5, label="Slice(s)")

ingredient1 = Ingredient(id=1, name="Salt", unit_id=2, aisle_id=3)
ingredient2 = Ingredient(id=2, name="Apple", unit_id=4, aisle_id=1)
ingredient3 = Ingredient(id=3, name="Eggs", unit_id=3, aisle_id=5)
ingredient4 = Ingredient(id=4, name="Salmon", unit_id=1, aisle_id=2)
ingredient5 = Ingredient(id=5, name="Bread", unit_id=5, aisle_id=4)

db.session.add_all([aisle1, aisle2, aisle3, aisle4, aisle5])
db.session.add_all([unit1, unit2, unit3, unit4, unit5])
db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5])

db.session.commit()

# s1 = Ingredient.query.filter_by(name="Apple").first()


# shopping1 = Shopping(id=1, ingredient_name=s1.name, aisle_name=s1.aisle.name, aisle_id = s1.aisle_id)

# db.session.add_all([aisle1, aisle2, aisle3, aisle4, aisle5])
# db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5])
# db.session.add(shopping1)

# db.session.commit()


# Shopping Test
# shopping1 = Shopping
