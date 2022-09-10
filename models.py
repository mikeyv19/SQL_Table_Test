from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Ingredient(db.Model):
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), db.ForeignKey("shopping.id"), nullable=False)
    aisle_id = db.Column(db.Integer, db.ForeignKey("aisle.id"))

    def __repr__(self):
        return "<Ingredient %r>" % self.name


class Aisle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), db.ForeignKey("shopping.id"))
    ingredients = db.relationship("Ingredient", backref="aisle")

    def __repr__(self):
        return "<Aisle %r>" % self.name

class Shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.relationship("Ingredient", backref="ingredient")
    aisle = db.relationship("Aisle", backref="aisle")

    def __repr__(self):
        return "<Shopping %r>" % self.name

def connect_db(app):
    db.app = app
    db.init_app(app)