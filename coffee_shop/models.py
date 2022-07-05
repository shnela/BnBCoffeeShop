# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
from datetime import datetime, timezone

from flask_login import UserMixin
from sqlalchemy import null
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


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
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), nullable=False,
                              default=lambda: datetime.now(tz=timezone.utc))
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def coffe_size_display_name(self):
        return COFFEE_SIZES.get(self.coffee_size, "Unknown size")

    def coffe_type_display_name(self):
        return COFFEE_TYPE.get(self.coffee_type, "Unknown type")


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    orders = db.relationship('CoffeeOrder', backref='customer', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
