# PDF RAG Assistant
A Retrieval-Augmented Generation (RAG) system that enables users to upload PDF documents and ask natural language questions. The system retrieves relevant context using semantic search and generates grounded answers using Google Gemini.

---
## How to run
### Clone the repository:
```text
git clone https://github.com/1affogato/chat-pdf-rag.git
cd chat-pdf-rag
```

### Create a virtual environment:
```text
python -m venv venv
```

### Activate the virtual environment:

#### Windows:
```text
venv\Scripts\activate
```

#### Linux / macOS:
```text
source venv/bin/activate
```

### Install dependencies:
```text
pip install -r requirements.txt
```
## Environment Variables
### Create a .env file in the project root:
```
GOOGLE_API_KEY=your_google_api_key
```
## Running the Backend
### Start FastAPI:
```
uvicorn main:app --reload
```

### API documentation:
http://127.0.0.1:8000/docs

### Running the Frontend
### Start Streamlit:
```
streamlit run app.py
```
#### Open:
http://localhost:8501

---

## Features 
- PDF document ingestion
- Text chunking using LangChain
- Semantic embeddings with Hugging Face
- Vector storage using ChromaDB
- Context retrieval through similarity search
- Question answering powered by Google Gemini
- REST API built with FastAPI
- Interactive API documentation with Swagger UI
---

## Tech Stack
- Python
- FastAPI
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Google Gemini
- PyPDF

---

## Future Improvements 
- FastAPI backend
- REST API endpoints
- Streamlit frontend
- Multi-document support
- Conversation memory
- Docker deployment

---

## Architecture
```text
PDF Upload
      │
      ▼
 Document Loader
      │
      ▼
 Text Chunking
      │
      ▼
 Embeddings (Hugging Face)
      │
      ▼
 ChromaDB Vector Store
      │
      ▼
 Similarity Search
      │
      ▼
 Google Gemini
      │
      ▼
     Answer
```

## API Endpoints
### Upload a PDF

#### POST /upload
Uploads and automatically indexes a PDF document.
Ask Questions

#### POST /ask
Receives a natural language question and returns an answer based on the indexed documents.

---

#### Example Request
```text
{
  "question": "What is an Artificial Neural Network?"
}
```

#### Example Response
```text
{
  "answer": "An Artificial Neural Network is a mathematical model that receives external inputs or inputs from other neurons, combines them, and produces an output to perform specific tasks."
}
```