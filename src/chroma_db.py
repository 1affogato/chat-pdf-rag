import os
import shutil
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma"

def save_to_chroma_db(chunks: list[Document], embedding_model) -> Chroma:
    # elimina la base de datos existente
    if os.path.exists(CHROMA_PATH):
        try:
            shutil.rmtree(CHROMA_PATH)
        except Exception as e:
            print("error deletng existing chroma directory")

    # inicia un nuevo objeto que contiene la nueva base de datos
    db = Chroma.from_documents(
        chunks, # chunks datos
        persist_directory= CHROMA_PATH, # directorio de la bd vectorial
        embedding = embedding_model
    )

    print(f"Saved {len(chunks)} documents at {CHROMA_PATH}")

    return db 