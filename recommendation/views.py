from flask import Flask, render_template, url_for, request
import sqlite3
import json
from urllib import parse
from sqlalchemy import create_engine
import os
import psycopg2
import logging as lg

import pandas as pd
app = Flask(__name__)
app.config.from_object('config')


from . import models
from config import SQLALCHEMY_DATABASE_URI

@app.route('/', methods =['GET','POST'])
@app.route('/?', methods =['GET','POST'])
@app.route('/index/', methods =['GET','POST'])
def index(movie=None,querry=None,results=None):

    if request.method == 'POST':
        movie= request.form['movie']
        if os.environ.get('DATABASE_URL') is None:
            conn = sqlite3.connect('app.db')

        else:
            parse.uses_netloc.append("postgres")
            url = parse.urlparse(SQLALCHEMY_DATABASE_URI)
            conn = psycopg2.connect(database=url.path[1:],user=url.username,
            password=url.password,host=url.hostname,port=url.port)


        c = conn.cursor()
        myneighbs = []
        results = []
        if len(movie)>0:
            query_df = pd.read_sql("SELECT neigbhoors FROM content WHERE original_title='%s'"%movie, con=conn)

            clean_row = query_df['neigbhoors'][0].replace("'", "\"")
            querry = json.loads(clean_row)
            neighb1 = querry['neighb1']
            neighb2 = querry['neighb2']
            neighb3 = querry['neighb3']
            neighb4 = querry['neighb4']
            neighb5 = querry['neighb5']
            myneighbs =[neighb1,neighb2,neighb3,neighb4,neighb5]

            for neighboor in myneighbs:
                query_df = pd.read_sql("SELECT moviesynthesis FROM content WHERE movie_index='%s'"%neighboor, con=conn)
                row2 = query_df['moviesynthesis'][0]
                clean_row2 = row2.replace("'", "\"")
                
                querry2 = json.loads(clean_row2)
                results.append(querry2)
        conn.close()

    return render_template('index.html',movie=movie,querry=querry,results=results)

@app.route('/movies_list/')
def movies_list():
    return render_template('movies_list.html')
