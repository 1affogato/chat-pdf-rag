# PDF RAG Assistant
A Retrieval-Augmented Generation (RAG) system that allows users to ask questions about PDF documents and receive context-aware answers based on the document content.

---

## Features 
- PDF document ingestion
- Text chunking using LangChain
- Semantic embeddings with Hugging Face
- Vector storage using ChromaDB
- Context retrieval through similarity search
- Question answering powered by Google Gemini

---

## Tech Stack
- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Google Gemini
- PyPDF

---

## Example

### Question
**What is an Artificial Neural Network?**

### Answer
An Artificial Neural Network is a mathematical model that receives external inputs or inputs from other neurons, combines them, and produces an output to perform specific tasks.

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
PDF Documents
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

- - - - - - - - - - - - - - - - - - - - - - - -
# Asistente RAG PDF

Un sistema de Retrieval-Augmented Generation (RAG) que permite a los usuarios realizar preguntas sobre documentos PDF y obtener respuestas basadas en el contenido del documento.

## Características
- Carga e ingestión de documentos PDF
- División de texto en fragmentos mediante LangChain
- Embeddings semánticos con Hugging Face
- Almacenamiento vectorial utilizando ChromaDB
- Recuperación de contexto mediante búsqueda por similitud
- Respuestas a preguntas impulsadas por Google Gemini

## Tecnologias
- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Google Gemini
- PyPDF

## Ejemplo

### Pregunta
**¿Qué es una Red Neuronal Artificial?**

### Respuesta
Una Red Neuronal Artificial es un modelo matemático que recibe entradas externas o provenientes de otras neuronas, las combina y genera una salida para realizar tareas específicas.

## Mejoras Futuras
- Backend con FastAPI
- Endpoints REST API
- Interfaz web con Streamlit
- Soporte para múltiples documentos
- Memoria conversacional
- Despliegue con Docker

## Arquitectura
```text
PDF Documents
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