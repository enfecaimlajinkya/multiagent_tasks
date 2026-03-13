# multiagent_tasks
Assignment 1: Multi‑Agent Research Assistant with MCP Integration

# Problem Statement
The objective of this project is to build a Multi-Agent Research Assistant that can answer user queries by coordinating multiple AI agents. The system uses a planner–research agent architecture where different agents collaborate to analyze a user question, perform information retrieval, and generate a final response.

The application demonstrates how LangGraph can orchestrate multiple agents, how external tools can be exposed using Model Context Protocol (MCP), and how the results can be delivered through a simple Streamlit user interface. The system also stores user interactions in PostgreSQL to maintain conversation history and allow future reuse.

This project helps demonstrate the fundamentals of agent-based AI systems, tool integration, and building a simple end-to-end application using modern AI frameworks.

# Workflow Steps
The system follows a multi-step workflow where each component performs a specific role in processing the user query.

User Input

The user enters a question or travel planning request in the Streamlit interface.

Planner Agent Execution

The planner agent receives the user query.

It analyzes the question and creates a research plan describing what information needs to be retrieved.

LangGraph Workflow

LangGraph manages the workflow and passes the generated plan from the planner agent to the research agent.

Research Agent Execution

The research agent takes the plan and calls an external tool via MCP to retrieve relevant information.

MCP Tool Invocation

The MCP server exposes a web search tool (DuckDuckGo).

The research agent uses this tool to fetch search results.

LLM Processing

The retrieved information is processed by the LLM (Groq model) to generate a clear and structured response.

Data Storage

The system stores the following information in PostgreSQL:

User question

Planner output

Research results

Final generated answer

Final Response

The final response is displayed to the user in the Streamlit UI.

# Architecture Diagram

User
  │
  ▼
Streamlit UI
  │
  ▼
LangGraph Workflow
  │
  ├──► Planner Agent
  │       │
  │       ▼
  │   Creates Search Plan
  │
  └──► Research Agent
          │
          ▼
      MCP Tool (Web Search)
          │
          ▼
       LLM Answer
          │
          ▼
     PostgreSQL Storage
          │
          ▼
       Final Output

# Tools used

Tools Used

The project uses the following technologies and frameworks:

AI / Agent Frameworks

LangGraph – Used to create and manage the multi-agent workflow.

LangChain – Provides tools and utilities for building LLM-powered applications.

Language Model

Groq LLM (Llama 3 models) – Used for reasoning, planning, and generating responses.

Tool Integration

Model Context Protocol (MCP) – Used to expose external tools and allow agents to call them.

DuckDuckGo Search Tool – Used for retrieving information from the web.

Backend

Django REST Framework – Provides simple API endpoints for interacting with the system programmatically.

Database

PostgreSQL – Stores user queries, planner outputs, research results, and final answers.

Frontend

Streamlit – Provides a simple and interactive web interface for users.

Development Tools

Python

Jupyter Notebook

draw.io – Used for creating architecture and workflow diagrams.

# Setup Instructions

1. Generate Groq API Key

This project uses Groq LLM for agent reasoning.

Visit the Groq console:
https://console.groq.com/keys

Generate a free API key.

Copy the generated API key.

2. Configure Environment Variables

Create a .env file in the project root directory:

A_1_MultiAgent_Research_Assistant_with_MCP_Integration/.env

Add your Groq API key in the following format:

GROQ_API_KEY=your_groq_api_key_here
3. Install Project Dependencies

All required libraries are listed in the requirements.txt file located at:

A_1_MultiAgent_Research_Assistant_with_MCP_Integration/requirements.txt

Open a command prompt or terminal in the project directory and run:

pip install -r requirements.txt

This will install all the required dependencies including:

LangGraph

LangChain

MCP

Streamlit

PostgreSQL connector

Groq SDK

DuckDuckGo search tools

4. Run the Application

After installing dependencies, run the Streamlit application:

python -m streamlit run ui/streamlit_app.py

5. Access the Web Interface

Once the application starts, Streamlit will launch the interface at:

http://localhost:8501

This will open the AI Travel Agent interface in your browser.

Using the Application

Users can interact with the AI Travel Agent by entering a travel planning request.

Provide details such as:

Destination location

Budget per person

Number of travelers

Trip duration (number of days and nights)

Travel class (Economy / Business)

Preferred hotel category (2★ / 3★ / 4★ / 5★ / 7★)

Currency for budget estimation

Example request:

Plan a 5-day trip to Paris for 2 people with a budget of $3000 per person, business class flights, and 4-star hotels.
How the System Responds

The system processes the request using a multi-agent workflow:

Planner Agent:-

Analyzes the travel request

Creates a structured plan including destinations, activities, and research requirements.

Research Agent:-

Uses tools exposed via MCP (Model Context Protocol) to gather relevant travel information.

Travel Plan Generation

Suggests destinations and attractions

Identifies suitable hotels

Estimates transportation options (flights, trains, buses, cabs)

Calculates an approximate travel budget

Final Output:-

Provides a detailed travel itinerary

Displays estimated costs in both:

User-specified currency

Local currency of the destination

Summary:-

This project demonstrates a Multi-Agent AI system where:

Agents collaborate using LangGraph

External tools are accessed via MCP

Travel research is performed dynamically

Conversations and results are stored in PostgreSQL

Users interact through a Streamlit-based interface

# Sample Output

Example user request:

Plan a 4-day trip to Paris for 2 people with a budget of $2500 per person and 4-star hotel preference.

Example system output:

Planner Output

Destination: Paris
Duration: 4 Days
Research Tasks:
- Find top attractions in Paris
- Identify 4-star hotels
- Suggest transportation options
- Estimate travel cost

Research Results

Top attractions include Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and Seine River Cruise.
Several 4-star hotels are available near the city center.
Public transportation includes metro, taxis, and buses.

Final Travel Plan

Day 1: Arrival in Paris, visit Eiffel Tower and evening Seine River Cruise.
Day 2: Louvre Museum, Champs-Élysées, Arc de Triomphe.
Day 3: Montmartre and Sacré-Cœur, local food tour.
Day 4: Notre-Dame Cathedral and shopping before departure.

Estimated Budget:
~$2400 per person (including accommodation, local transport, and attractions).

The system presents the final result in the Streamlit interface, along with the planner decision and research information.