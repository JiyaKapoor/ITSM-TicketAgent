# basically the KB articles that we have are .md files (YAML) 
# these files if splitted simply using recursive character splitter then the context will be lost, the issue may get merged with symptoms etc
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader=UnstructuredMarkdownLoader("kb_article.md",mode="elements")
raw_docs=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks=splitter.split_documents(raw_docs)
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(f"Content : {chunk.page_content}")
    print(f"Metadata: {chunk.metadata}")
 
