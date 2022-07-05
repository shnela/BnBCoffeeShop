from flask import render_template, redirect

from . import bp
from .forms import OrderCoffeeForm

from ..models import CoffeeOrder
from .. import db



@bp.route("/coffee")
def list_coffee_orders():
    orders = CoffeeOrder.query.all()
    return render_template("coffee_orders.html", coffee_orders=orders)


@bp.route("/coffee/new", methods=['GET', 'POST'])
def order_coffee():
    form = OrderCoffeeForm()
    if form.validate_on_submit():
        form_data = form.data
        order = CoffeeOrder(
            coffee_size=form_data['coffee_size'],
            coffee_type=form_data['coffee_type'],
            customer_username=form_data['customer_username'],
        )
        db.session.add(order)
        db.session.commit()
        
        return redirect('/')
    return render_template('order.html', form=form)
