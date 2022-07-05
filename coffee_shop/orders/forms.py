from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField, StringField, SelectField
from wtforms.validators import DataRequired, ValidationError


COFFEE_SIZES = (
    ('S', 'small'),
    ('L', 'large'),
    ('XL', 'x-large'),
)
COFFEE_TYPE = (
    ('L', 'latte'),
    ('C', 'capucino'),
    ('A', 'americana'),
    ('E', 'espresso'),
)

class OrderCoffeeForm(FlaskForm):
    coffee_size = SelectField(
        'Coffe Size',
        choices=COFFEE_SIZES,
        validators=[DataRequired()]
    )
    coffee_type = SelectField(
        'Coffee type',
        choices=COFFEE_TYPE,
        validators=[DataRequired()]
        )
    customer_username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')
