# Semantic Search Engine with Vector Database (PGVector)

# Problem Statement

Traditional search systems rely on keyword matching, which often fails when users search using synonyms, paraphrased queries, or related concepts. For example, searching for “romantic city in Europe” may not return results if the document only contains the phrase “Paris travel guide”.

The objective of this project is to build a Semantic Search Engine that can understand the meaning of the user query instead of relying only on exact keyword matches. The system uses vector embeddings and a vector database (PostgreSQL with pgvector) to retrieve documents that are semantically similar to the query.

The application demonstrates the difference between:

Keyword-based search

Embedding-based semantic search

through an interactive Streamlit user interface.

# Workflow Steps

The overall workflow of the Semantic Search Engine is as follows:

1. Document Preparation

A dataset of documents is stored in a CSV file containing document titles and text content.

2. Document Ingestion

The ingestion script reads each document from the dataset and processes it for storage.

3. Embedding Generation

Each document is converted into a vector embedding using the Sentence Transformer model (all-MiniLM-L6-v2).
These embeddings capture the semantic meaning of the text.

4. Vector Storage

The generated embeddings are stored in PostgreSQL using the pgvector extension, allowing efficient similarity search.

5. User Query Input

The user enters a search query through the Streamlit web interface.

6. Keyword Search Execution

The system performs a traditional keyword search using SQL text matching:

ILIKE '%query%'

This retrieves documents containing the exact search terms.

7. Semantic Search Execution

The user query is converted into an embedding vector, and PostgreSQL performs a vector similarity search against stored document embeddings using cosine distance.

8. Results Comparison

The Streamlit interface displays:

Keyword search results

Semantic search results

side-by-side, allowing users to clearly compare both approaches.

# Workflow Diagram

User
  │
  ▼
Streamlit UI
  │
  ▼
Search Query
  │
  ├──► Keyword Search
  │       │
  │       ▼
  │   PostgreSQL Query
  │   (ILIKE / Text Match)
  │       │
  │       ▼
  │   Keyword Results
  │
  └──► Semantic Search
          │
          ▼
      Query Embedding
   (Sentence Transformer - all-MiniLM-L6-v2)
          │
          ▼
      PostgreSQL + pgvector
      Vector Similarity Search
          │
          ▼
      Top Similar Documents
          │
          ▼
      Semantic Results
          │
          ▼
   Display Results Side-by-Side

# Tools Used

The project uses the following technologies and frameworks:

Programming Language:

Python version 3.10.9

Sentence Transformers – used to generate semantic embeddings for documents and queries (all-MiniLM-L6-v2)

Vector Database:

PostgreSQL

pgvector extension – used to store and query vector embeddings efficiently.

Backend Processing:

Python scripts for document ingestion and search execution.

Web Interface:

Streamlit – used to create an interactive user interface for querying and displaying results.

Data Handling:

Pandas – for reading and processing CSV datasets.

# Setup Instructions

Follow the steps below to set up and run the Semantic Search Engine with Vector Database.
________________________________________
1. Project Directory
Navigate to the project directory:
A_2_Semantic_Search_Engine_with_Vector_Database
This directory contains the backend scripts, dataset, and Streamlit user interface for the semantic search application.
________________________________________
2. Install Project Dependencies
All required libraries are listed in the requirements.txt file located at:
A_2_Semantic_Search_Engine_with_Vector_Database/requirements.txt
Open a command prompt or terminal in the project directory and run:
pip install -r requirements.txt
This will install all the required dependencies including:
•	Streamlit
•	PostgreSQL connector (psycopg2)
•	pgvector support
•	Sentence Transformers
•	NumPy
•	Pandas
•	Python utilities for database connectivity
These libraries are required to generate embeddings, perform vector similarity search, and run the web interface.
________________________________________
3. Prepare the Dataset
The project uses a CSV file containing sample documents for search.
The dataset file is located at:
A_2_Semantic_Search_Engine_with_Vector_Database
└── semantic_search_engine
    └── data
        └── documents.csv
Each row in the file contains:
•	title – document title
•	content – text content of the document
Example format:
title,content
Paris Travel Guide,Paris is famous for the Eiffel Tower and romantic culture.
Tokyo Food Guide,Tokyo offers sushi ramen and world class street food.
You can modify this file and add any passages or text content to test keyword and semantic search functionality.
________________________________________
4. Generate Document Embeddings
Before running the search system, the documents must be converted into vector embeddings and stored in the PostgreSQL database.
Run the ingestion script:
python scripts/ingest_documents.py
This script will:
1.	Read documents from the CSV file.
2.	Generate vector embeddings using the Sentence Transformer model (all-MiniLM-L6-v2).
3.	Store the document text and embeddings in PostgreSQL with the pgvector extension.
________________________________________
5. Run the Application
Navigate to the application root folder:
A_2_Semantic_Search_Engine_with_Vector_Database/semantic_search_engine
Then start the Streamlit application:
python -m streamlit run ui/app.py
________________________________________
6. Access the Web Interface
Once the application starts, Streamlit will launch the interface at:
http://localhost:8501
This will open the Semantic Search vs Keyword Search interface in your browser.
________________________________________
Using the Application
Users can interact with the system by entering a search query.
The system performs two types of search simultaneously:
1. Keyword Search
•	Uses traditional SQL text matching.
•	Searches documents using:
ILIKE '%query%'
•	Returns documents containing the exact keywords.
________________________________________
2. Semantic Search
Semantic search works differently:
1.	The user query is converted into a vector embedding.
2.	The embedding is compared with stored document embeddings.
3.	PostgreSQL pgvector calculates similarity using cosine distance.
Example similarity query:
embedding <=> query_embedding
This allows the system to retrieve documents with similar meaning, even if the exact words are different.
________________________________________
Example Queries
Try searching with queries such as:
romantic city in europe
japanese noodles
snow mountains vacation
famous landmarks in paris

Expected behavior
Search Type	Result
Keyword Search	Matches exact words
Semantic Search	Finds documents with similar meaning
For example:
Query:
romantic city in europe
Keyword search may return no results, but semantic search can correctly identify:
Paris Travel Guide
because the embedding model understands the semantic relationship between the words.
________________________________________
System Output
The interface displays:
•	Keyword search results
•	Semantic search results
•	Results shown side-by-side for comparison
This clearly demonstrates the advantage of vector-based semantic search over traditional keyword matching.

# Sample Output

Below is an example demonstrating the difference between keyword search and semantic search.

Example Query
romantic city in europe
Keyword Search Result

Keyword search may return no results if the document does not contain the exact words "romantic city".

Semantic Search Result

Semantic search identifies relevant documents based on meaning.

Example result:

Title: Paris Travel Guide

Content:
Paris is famous for the Eiffel Tower and its romantic culture. 
It is considered one of the most romantic cities in the world.
Result Comparison
Search Type	Result
Keyword Search	No exact match
Semantic Search	Returns Paris Travel Guide

This demonstrates how semantic search understands the meaning of the query and retrieves relevant documents even when the exact keywords are not present.
Assignment 2: Semantic Search Engine with Vector Database



