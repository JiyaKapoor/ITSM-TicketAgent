from langchain_mistralai import ChatMistralAI
from retriever import retrieve
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")
def format_docs(docs):
    return "\n\n---\n\n".join(
        f"[Source: {doc.metadata.get('source', 'unknown')}]\n{doc.page_content}"
        for doc in docs
    )
def generate_resolution(query):
    llm=ChatMistralAI(model="mistral-large-latest", temperature=0.1)
    prompt = PromptTemplate.from_template("""
        You are an ITSM support agent. Answer using ONLY the context below.

        CONTEXT:
        {context}

        QUESTION:
        {question}

        ANSWER:
        """)
    docs=retrieve(query)
    context=format_docs(docs)
    response=prompt | llm | StrOutputParser()
    return response.invoke({"context":context,"question":query})


    
     
