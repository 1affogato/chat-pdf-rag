from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

DOCUMENTS_PATH = "documents"

# funcion que tokeniza los documentos (los divide) y los retorna 

def chunks_pdfs() -> list[Document]:
    documentLoader = PyPDFDirectoryLoader(DOCUMENTS_PATH)
    documents = documentLoader.load()

    textSplitter = RecursiveCharacterTextSplitter(
        chunk_size = 800, # cantidad de caracteres de cada chunk
        chunk_overlap = 100, # cantidad de caracteres que van a estar superpuestos en cada chunk, que mantengan conexion
        length_function = len, # funcion de longitud para dividir
        add_start_index = True # indice inicial a los chunks
    )

    chunks = textSplitter.split_documents(documents)

    return chunks