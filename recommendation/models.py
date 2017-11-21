#import enum
from flask_sqlalchemy import SQLAlchemy
import logging as lg
import sqlite3
import pandas as pd
import psycopg2
import os

from .views import app

# Create database connection object
#db = SQLAlchemy(app)



def init_db():

    if os.environ.get('DATABASE_URL') is None:
        db = SQLAlchemy(app)
        conn = sqlite3.connect('app.db')

    else:
        from urllib import parse
        db = SQLAlchemy(app)
        parse.uses_netloc.append("postgres")
        url = parse.urlparse(os.environ["DATABASE_URL"])
        conn = psycopg2.connect(database=url.path[1:],user=url.username,
        password=url.password,host=url.hostname,port=url.port)
        db = SQLAlchemy(app)
        #db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)

    db.drop_all()
    db.create_all()


    c = conn.cursor()
    c.executescript('drop table if exists Content;')

    df = pd.read_csv('recommandation_system_light.csv')
    df.to_sql('Content', conn, if_exists='append', index=False)

    db.session.commit()
    #Content.query.all()
    lg.warning('Database initialized!')
