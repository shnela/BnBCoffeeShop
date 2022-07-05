# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
from . import db


COFFEE_SIZES = {
    'S': 'small',
    'L': 'large',
    'XL': 'x-large',
}
COFFEE_TYPE = {
    'L': 'latte',
    'C': 'capucino',
    'A': 'americana',
    'E': 'espresso',
}

class CoffeeOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coffee_size = db.Column(db.String(3))
    coffee_type = db.Column(db.String(3))
    customer_username = db.Column(db.String(80), nullable=False)

    def coffe_size_display_name(self):
        return COFFEE_SIZES.get(self.coffee_size, "Unknown size")

    def coffe_type_display_name(self):
        return COFFEE_TYPE.get(self.coffee_type, "Unknown type")
