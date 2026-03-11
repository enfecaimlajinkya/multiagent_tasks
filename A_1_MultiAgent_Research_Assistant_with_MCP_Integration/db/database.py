import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    database="travel_agent",
    user="postgres",
    password="root",
    port="5432"
)

cursor = conn.cursor()


def check_cache(question):

    cursor.execute(
        "SELECT final_answer FROM travel_memory WHERE question=%s",
        (question,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return None


def save_result(state):

    cursor.execute(
        """
        INSERT INTO travel_memory
        (question, plan, research_result, final_answer)
        VALUES (%s,%s,%s,%s)
        """,
        (
            str(state["question"]),
            str(state["plan"]),
            str(state["research_result"]),
            str(state["final_answer"])
        )
    )

    conn.commit()