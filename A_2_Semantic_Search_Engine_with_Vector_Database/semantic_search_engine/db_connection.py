import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="semantic_search",
    user="postgres",
    password="root"
)

cursor = conn.cursor()