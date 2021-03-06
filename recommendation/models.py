from flask_sqlalchemy import SQLAlchemy
import logging as lg
import sqlite3
import pandas as pd
import psycopg2
import os

from .views import app
from config import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


def init_db():
    db.drop_all()
    db.create_all()

    if os.environ.get('DATABASE_URL') is None:

        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.executescript('drop table if exists content;')

        df = pd.read_csv('recommandation_system_light.csv',encoding ='utf-8')
        df.to_sql('content', conn, if_exists='append', index=False)

        db.session.commit()
        lg.warning('Database initialized!')

    else:
        from urllib import parse
        from sqlalchemy import create_engine

        parse.uses_netloc.append("postgres")
        url = parse.urlparse(SQLALCHEMY_DATABASE_URI)
        conn = psycopg2.connect(database=url.path[1:],user=url.username,
        password=url.password,host=url.hostname,port=url.port)

        #c = conn.cursor()
        #c.execute("DROP TABLE IF EXISTS content;")


        df = pd.read_csv('recommandation_system_light.csv',encoding ='utf-8')
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        #df.to_sql("content", engine)
        df.to_sql("content", engine, if_exists='replace')

        db.session.commit()
        lg.warning('Database initialized!')
        lg.warning('%s'%SQLALCHEMY_DATABASE_URI)
