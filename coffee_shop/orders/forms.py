from flask_wtf import FlaskForm
# https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired


from ..models import COFFEE_SIZES, COFFEE_TYPE



class OrderCoffeeForm(FlaskForm):
    coffee_size = SelectField(
        'Coffe Size',
        choices=COFFEE_SIZES.items(),
        validators=[DataRequired()]
    )
    coffee_type = SelectField(
        'Coffee type',
        choices=COFFEE_TYPE.items(),
        validators=[DataRequired()]
        )
    submit = SubmitField('Submit')
