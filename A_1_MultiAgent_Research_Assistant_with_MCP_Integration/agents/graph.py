from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END

from agents.planner import planner_agent
from agents.research import research_agent


class AgentState(TypedDict):

    question: str
    plan: Optional[str]
    research_result: Optional[str]
    final_answer: Optional[str]


def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planner_agent)
    workflow.add_node("research", research_agent)

    workflow.set_entry_point("planner")

    workflow.add_edge("planner", "research")
    workflow.add_edge("research", END)

    return workflow.compile()