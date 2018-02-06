import psycopg2
import sys
import pandas as pd


#Define our connection string
conn_string = "host='localhost' dbname='postgres' user='postgres' password='Raerblapa1.'"

# print the connection string we will use to connect
print("Connecting to database\n	->%s" %(conn_string))

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print("Connected!\n")


start = 3

mydf = pd.read_sql("""SELECT * FROM public.movies WHERE movie_id < '%s' """%start, con=conn)

print(mydf)
print(mydf['movie_name'][0])

mydf = pd.read_sql("""SELECT movie_name FROM public.movies WHERE movie_id =2 """, con=conn)

print(mydf['movie_name'][0])
#print(mydf['movie_name'])

#for i in mydf:
#    print(i)
