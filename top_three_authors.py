import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)

cursor = db.cursor()

