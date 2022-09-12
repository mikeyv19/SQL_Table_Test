from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "fake"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///action.db"
db = SQLAlchemy(app)


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    act = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(20), nullable=False)


def __repr__(self):
    return "<act %r" % self.act


class StatusForm(FlaskForm):
    time = StringField("Time", validators=[DataRequired()])
    act = StringField("Action", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = StatusForm()
    entry_to_update = Action.query.get_or_404(id)
    if request.method == "POST":
        entry_to_update.act = request.form["act"]
        entry_to_update.time = request.form["time"]
        try:
            db.session.commit()
            flash("Entry updated successfully!")
            return render_template(
                "update.html", form=form, entry_to_update=entry_to_update
            )
        except:
            flash("Error! Looks like there was a problem. Try again.")
            return render_template(
                "update.html", form=form, entry_to_update=entry_to_update
            )
    else:
        return render_template(
            "update.html", form=form, entry_to_update=entry_to_update
        )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/status", methods=["GET", "POST"])
def status():
    act = None
    time = None
    form = StatusForm()
    if form.validate_on_submit():
        update = Action(act=form.act.data, time=form.time.data)
        db.session.add(update)
        db.session.commit()
        act = form.act.data
        form.act.data = ""
        time = form.time.data
        form.time.data = ""
        flash("Form Submitted Successfully")
    our_actions = Action.query.order_by(Action.id.desc())
    return render_template(
        "status.html", form=form, act=act, time=time, our_actions=our_actions
    )


@app.route("/sitback")
def sitback():
    return render_template("sitback.html")


@app.route("/intervention")
def intervention():
    return render_template("intervention.html")
