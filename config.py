import os

#RUN 1
#Chemin vers la base de données :
#basedir = os.path.abspath(os.path.dirname(__file__))
#On indique que l'on utilise sqlite et que notre base de données s'appelle "app.db"
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

#RUN FINAL :
# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
