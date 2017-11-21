#import enum
from flask_sqlalchemy import SQLAlchemy
import logging as lg
import sqlite3
import pandas as pd
import psycopg2

from .views import app

# Create database connection object
db = SQLAlchemy(app)

def init_db():
    db.drop_all()
    db.create_all()

    if os.environ.get('DATABASE_URL') is None:
        conn = sqlite3.connect('app.db')

    else:
        conn = psycopg2.connect('app.db')

    c = conn.cursor()
    c.executescript('drop table if exists Content;')

    df = pd.read_csv('recommandation_system_light.csv')
    df.to_sql('Content', conn, if_exists='append', index=False)

    db.session.commit()
    #Content.query.all()
    lg.warning('Database initialized!')
