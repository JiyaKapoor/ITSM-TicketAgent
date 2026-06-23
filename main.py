from embedder import embed_chunks
from loader import load_and_chunk
from retriever import retrieve

if __name__ == "__main__":
    query="how do I fix exclusive lock error in Access?"
    results = retrieve(query)
    
    for i, doc in enumerate(results):
        print(f"\n--- Result {i+1} ---")
        print(f"Content : {doc.page_content}")
        print(f"Metadata: {doc.metadata}")