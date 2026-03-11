from db_connection import cursor
from embedding_utils import get_embedding

def semantic_search(query):

    query_embedding = get_embedding(query)

    cursor.execute("""
        SELECT title, content,
        embedding <=> %s::vector AS distance
        FROM documents
        ORDER BY distance
        LIMIT 5
    """, (query_embedding,))

    results = cursor.fetchall()

    return results