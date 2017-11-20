from flask import Flask

from .views import app #On a d�j� cr�� l'objet "app" dans le script views.py
from . import models

models.db.init_app(app)
@app.cli.command()
def init_db():
    models.init_db()
@app.cli.command()
def get_db():
    models.get_db()
