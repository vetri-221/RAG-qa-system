from src.search import RAGSearch

if __name__ == "__main__":

    rag_search = RAGSearch()

    query = input("Ask your question: ")

    answer = rag_search.search_and_summarize(
        query,
        top_k=5
    )

    print("\nAnswer:")
    print(answer)

    