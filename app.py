from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
if __name__ == '__main__':
    # docs=load_all_documents('data')
    store=FaissVectorStore("faiss_store")
    # documents=load_all_documents('data')
    # store.build_from_documents(documents)
    store.load()
    # print(store.query('what is attention is all you need ',top_k=2))

    rag_search=RAGSearch()
    query="what is Simple count-based embeddings"
    summary=rag_search.search_and_summarize(query,top_k=3)
    print('summary:',summary)

    