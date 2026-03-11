import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.graph import build_graph
from db.database import check_cache, save_result

graph = build_graph()

st.title("AI Travel Planner")

question = st.text_input(
    "Enter your travel request",
    placeholder="Plan a 5 day trip to Paris under $2000"
)

if st.button("Generate Plan"):

    cached = check_cache(question)

    if cached:

        st.success("Cached Result")
        st.write(cached)

    else:

        result = graph.invoke({
            "question": question
        })

        save_result(result)

        st.subheader("Planner Output")
        st.write(result["plan"])

        st.subheader("Research Result")
        st.write(result["research_result"])

        st.subheader("Final Travel Plan")
        st.success(result["final_answer"])