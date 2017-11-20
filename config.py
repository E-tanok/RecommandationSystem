import os

#Chemin vers la base de données :
basedir = os.path.abspath(os.path.dirname(__file__))
#On indique que l'on utilise sqlite et que notre base de données s'appelle "app.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
