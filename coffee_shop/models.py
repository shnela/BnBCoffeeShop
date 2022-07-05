# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
from . import db


class CoffeeOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coffee_size = db.Column(db.String(3))
    coffee_type = db.Column(db.String(3))
    customer_username = db.Column(db.String(80), nullable=False)
