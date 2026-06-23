from embedder import embed_chunks
from loader import load_and_chunk
from retriever import retrieve
from resolution import generate_resolution

if __name__ == "__main__":
    query="how do I fix exclusive lock error in Access?"
    resolution=generate_resolution(query)
    print(resolution)
    