import os
from src.text_processor import chunks_pdfs
from src.chroma_db import save_to_chroma_db
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# tokeniza el pdf
processed_documents = chunks_pdfs()

# modelo de embedding
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# base de datos vectorial
db = save_to_chroma_db(processed_documents, embedding_model)

query = "Que es una RNA"

# busca la similaridad con el quert y k=3 busca los 3 elementos con mas similitud
docs = db.similarity_search(query, k=3)

# concatena los contenidos del documento de docs
context = "\n\n----\n\n".join([doc.page_content for doc in docs])

# imprime contexto
# print(context)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

PROMPT_TEMPLATE = """
Answer the question using only the information provided in the context.

Context:
{context}

Question:
{question}

Instructions:
- Provide a clear and detailed answer.
- Do not include information that is not present in the context.
- If the answer is not in the context, say so.
"""

prompt = PROMPT_TEMPLATE.format(
    context=context,
    question=query
)

response = llm.invoke(prompt)

print(response.content)