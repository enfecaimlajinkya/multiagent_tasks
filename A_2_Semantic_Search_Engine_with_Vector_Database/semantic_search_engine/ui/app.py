import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.keyword_search import keyword_search
from scripts.semantic_search import semantic_search


st.title("Semantic Search vs Keyword Search")

query = st.text_input("Enter search query")

if st.button("Search"):

    col1, col2 = st.columns(2)

    keyword_results = keyword_search(query)

    semantic_results = semantic_search(query)

    with col1:
        st.subheader("Keyword Search")

        for r in keyword_results:
            st.write("###", r[0])
            st.write(r[1])

    with col2:
        st.subheader("Semantic Search")

        for r in semantic_results:
            st.write("###", r[0])
            st.write(r[1])
            st.write("Distance:", r[2])