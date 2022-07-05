from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import bp
from .forms import OrderCoffeeForm

from ..models import CoffeeOrder
from .. import db



@bp.route("/coffee")
@login_required
def list_coffee_orders():
    orders = CoffeeOrder.query.filter(CoffeeOrder.customer_id == current_user.id)
    return render_template("coffee_orders.html", coffee_orders=orders)


@bp.route("/coffee/new", methods=['GET', 'POST'])
@login_required
def order_coffee():
    form = OrderCoffeeForm()
    if form.validate_on_submit():
        form_data = form.data
        order = CoffeeOrder(
            coffee_size=form_data['coffee_size'],
            coffee_type=form_data['coffee_type'],
            customer_id=current_user.id,
        )
        db.session.add(order)
        db.session.commit()
        
        return redirect('/')
    return render_template('order.html', form=form)


@bp.route("/coffee/complete/<int:order_id>/")
@login_required
def complete_coffee_order(order_id):
    order = CoffeeOrder.query.get_or_404(order_id)
    order.completed = True
    db.session.add(order)
    db.session.commit()
    return redirect(url_for('orders.list_coffee_orders'))