from models import Ingredient, Aisle, Shopping, connect_db, db
from main import app

db.drop_all()
db.create_all()

aisle1 = Aisle(id=1, name="Produce")
aisle2 = Aisle(id=2, name="Seafood")
aisle3 = Aisle(id=3, name="7")
aisle4 = Aisle(id=4, name="14")
aisle5 = Aisle(id=5, name="Dairy")

ingredient1 = Ingredient(id=1, name="Salt", aisle_id=3)
ingredient2 = Ingredient(id=2, name="Apple", aisle_id=1)
ingredient3 = Ingredient(id=3, name="Eggs", aisle_id=5)
ingredient4 = Ingredient(id=4, name="Salmon", aisle_id=2)
ingredient5 = Ingredient(id=5, name="Bread", aisle_id=4)

db.session.add_all([aisle1, aisle2, aisle3, aisle4, aisle5])
db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5])

db.session.commit()

s1 = Ingredient.query.filter_by(name="Apple").first()
print(s1.name)
print(s1.aisle.name)
print(s1.aisle_id)

shopping1 = Shopping(id=1, ingredient_name=s1.name, aisle_name=s1.aisle.name, aisle_id = s1.aisle_id)

# db.session.add_all([aisle1, aisle2, aisle3, aisle4, aisle5])
# db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5])
db.session.add(shopping1)

db.session.commit()


# Shopping Test
# shopping1 = Shopping
