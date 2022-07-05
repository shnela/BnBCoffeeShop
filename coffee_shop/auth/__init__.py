from flask import Blueprint

bp = Blueprint('auth', __name__, template_folder='templates')

from . import views  # views must be registered
