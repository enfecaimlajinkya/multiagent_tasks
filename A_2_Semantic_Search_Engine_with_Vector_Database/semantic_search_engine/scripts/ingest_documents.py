import sys
import os
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connection import conn, cursor
from embedding_utils import get_embedding

# get absolute path to documents.csv
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "data", "documents.csv")

with open(csv_path, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        title = row["title"]
        content = row["content"]

        embedding = get_embedding(content)

        cursor.execute("""
            INSERT INTO documents(title,content,embedding)
            VALUES (%s,%s,%s)
        """,(title,content,embedding))

        conn.commit()

        print("Inserted:", title)