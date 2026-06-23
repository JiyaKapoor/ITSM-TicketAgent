#this function basically retrieves top k embedded chunks from the db
from langchain_mistralai import MistralAIEmbeddings
from langchain_postgres import PGVector
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")
CONNECTION_STRING="postgresql://postgres:JiyaKapoor1409@db.djhsvigtouwtlzddfqbr.supabase.co:5432/postgres"
def retrieve(query):
    embeddings=MistralAIEmbeddings(model="mistral-embed")
    vector_store=PGVector(embeddings=embeddings,connection=CONNECTION_STRING,collection_name="kb_articles")
    return vector_store.as_retriever(search_kwargs={"k":3}).invoke(query)
