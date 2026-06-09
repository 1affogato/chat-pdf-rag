from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from src.services.text_processor import chunks_pdfs
from src.services.chroma_db import save_to_chroma_db
from dotenv import load_dotenv

processed_documents = chunks_pdfs()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = save_to_chroma_db(
    processed_documents,
    embedding_model
)

load_dotenv()

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


def ask_rag(question: str):

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n\n----\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content

def rebuild_database():

    processed_documents = chunks_pdfs()

    save_to_chroma_db(
        processed_documents,
        embedding_model
    )