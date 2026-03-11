from agents.graph import build_graph
from db.database import check_cache, save_result

graph = build_graph()


def run():

    question = input("Enter travel request: ")

    cached = check_cache(question)

    if cached:

        print("\nFrom Cache:\n", cached)
        return

    result = graph.invoke({
        "question": question
    })

    save_result(result)

    print("\nPlanner Output:\n", result["plan"])
    print("\nFinal Travel Plan:\n", result["final_answer"])


if __name__ == "__main__":

    run()