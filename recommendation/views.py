from flask import Flask, render_template, url_for, request
import sqlite3
import json
from urllib import parse
from sqlalchemy import create_engine
import os
import psycopg2
#from flask import g

app = Flask(__name__)
app.config.from_object('config')
#from .utils import find_content

from . import models
#def index(movie=None,movie_to_display=None):
#if movie!=None :
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
            url = parse.urlparse(os.environ["DATABASE_URL"])
            conn = psycopg2.connect(database=url.path[1:],user=url.username,
            password=url.password,host=url.hostname,port=url.port)

        c = conn.cursor()
        myneighbs = []
        results = []

        for row in c.execute("""SELECT neigbhoors FROM DATABASE.content WHERE original_title='%s'""" % movie):
            clean_row = row[0].replace("'", "\"")
            querry = json.loads(clean_row)
            neighb1 = querry['neighb1']
            neighb2 = querry['neighb2']
            neighb3 = querry['neighb3']
            neighb4 = querry['neighb4']
            neighb5 = querry['neighb5']
            myneighbs =[neighb1,neighb2,neighb3,neighb4,neighb5]

        for neighboor in myneighbs:
            for row2 in c.execute("""SELECT moviesynthesis FROM DATABASE.content WHERE movie_index='%s'""" % neighboor):
                clean_row2 = row2[0].replace("'", "\"")
                querry2 = json.loads(clean_row2)
                results.append(querry2)
        conn.close()

    return render_template('index.html',movie=movie,querry=querry,results=results)
