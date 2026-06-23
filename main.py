from embedder import embed_chunks
from loader import load_and_chunk

if __name__ == "__main__":
    # step 1 — load and chunk
    chunks = load_and_chunk("kb_article.md")
    print(f"Split into {len(chunks)} chunks")

    # step 2 — embed and store
    vector_store = embed_chunks(chunks)
    print("Stored in Supabase successfully")