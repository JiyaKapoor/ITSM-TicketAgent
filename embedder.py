from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_postgres import PGVector
import os
load_dotenv()
SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_KEY=os.getenv("SUPABASE_KEY")
MISTRAL_API_KEY=os.getenv("MISTRAL_API_KEY")
CONNECTION_STRING="postgresql://postgres:JiyaKapoor1409@db.djhsvigtouwtlzddfqbr.supabase.co:5432/postgres"
os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY
def embed_chunks(chunks):
    embeddings=MistralAIEmbeddings(model="mistral-embed")
    vector_store=PGVector.from_documents(documents=chunks,embedding=embeddings,connection=CONNECTION_STRING,collection_name="kb_articles",use_jsonb=True)