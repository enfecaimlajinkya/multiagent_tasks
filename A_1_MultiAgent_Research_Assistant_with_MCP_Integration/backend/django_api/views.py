from rest_framework.decorators import api_view
from rest_framework.response import Response

from agents.graph import build_graph
from db.database import check_cache, save_result

graph = build_graph()


@api_view(["POST"])
def travel_agent(request):

    question = request.data.get("question")

    cached = check_cache(question)

    if cached:
        return Response({
            "answer": cached,
            "source": "cache"
        })

    result = graph.invoke({
        "question": question
    })

    save_result(result)

    return Response({
        "plan": result["plan"],
        "research": result["research_result"],
        "answer": result["final_answer"]
    })