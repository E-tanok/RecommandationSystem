#import enum
from flask_sqlalchemy import SQLAlchemy
import logging as lg
import sqlite3
import pandas as pd

from .views import app

# Create database connection object
db = SQLAlchemy(app)

#On créé une nouvelle classe qui hérite de "enum" : https://docs.python.org/3/library/enum.html
#class Gender(enum.Enum):
    #female = 0
    #male = 1
    #other = 2


#On créé une classe "Content" qui hérite de db.Model, ce qui permettra de créer des tables par la suite
"""
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    moviesynthesis = db.Column(db.String(200), nullable=False)
    neigbhoors = db.Column(db.String(200), nullable=False)

    def __init__(self,title, description, gender, link):
        self.title = title
        self.moviesynthesis = description
        self.neigbhoors = gender
"""
def init_db():
    db.drop_all()
    db.create_all()

    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.executescript('drop table if exists Content;')

    df = pd.read_csv('recommandation_system_light.csv')
    df.to_sql('Content', conn, if_exists='append', index=False)



    db.session.commit()
    #Content.query.all()
    lg.warning('Database initialized!')


"""
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)

    def __init__(self,title, description, gender, link):
        self.title = title
        self.description = description
        self.gender = gender
        self.link = link

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("scary movie","film humour parodie horreur","comedie","www.scarymovie"))
    db.session.add(Content("hitch","film comedie romance","romance","www.hitch"))
    db.session.commit()
    #Content.query.all()
    lg.warning('Database initialized!')
"""
