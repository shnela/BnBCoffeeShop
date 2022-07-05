import os

CURRENT_DIR = os.path.dirname(__file__)


class Config:
    SECRET_KEY = "random-value-1234-fdsfdsa980"

    # FlaskDebugTolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(CURRENT_DIR, '..', 'test.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
