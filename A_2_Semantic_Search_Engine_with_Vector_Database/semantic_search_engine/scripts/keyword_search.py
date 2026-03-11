from db_connection import cursor

def keyword_search(query):

    cursor.execute(
    """
    SELECT title,content
    FROM documents
    WHERE content ILIKE %s
    LIMIT 5
    """,
    ('%' + query + '%',)
    )

    results = cursor.fetchall()

    return results