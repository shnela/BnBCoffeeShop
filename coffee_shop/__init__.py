# https://flask.palletsprojects.com/en/2.1.x/patterns/packages/?highlight=modular#simple-packages
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()

# initialize applications
# https://flask.palletsprojects.com/en/2.1.x/extensiondev/#the-extension-class-and-initialization
# https://bootstrap-flask.readthedocs.io/en/stable/basic/#initialization
Bootstrap5(app)
# https://flask-debugtoolbar.readthedocs.io/en/latest/#usage
toolbar = DebugToolbarExtension(app)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
db = SQLAlchemy(app)
# https://flask-login.readthedocs.io/en/latest/#configuring-your-application
login_manager.init_app(app)



# blueprints registration
# https://flask.palletsprojects.com/en/2.1.x/blueprints/
from .auth import bp as auth_bp
app.register_blueprint(auth_bp)
from .orders import bp as orders_bp
app.register_blueprint(orders_bp, url_prefix='/orders')

# index HTML
@app.route("/")
def index():
    return render_template("base.html")

db.create_all()
