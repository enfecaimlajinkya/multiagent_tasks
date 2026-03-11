from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()


llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0
)


def planner_agent(state):

    question = state["question"]

    prompt = f"""
You are a travel planning assistant.

Analyze the user's travel request and generate a plan.

User request:
{question}

Return:
Destination
Duration
Budget (if mentioned)
Research tasks needed.
"""

    response = llm.invoke(prompt)

    return {
        "plan": response.content.strip()
    }