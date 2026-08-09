# DocuMind AI

DocuMind AI is an AI-powered document intelligence platform that allows users to upload documents and interact with them using a Retrieval-Augmented Generation (RAG) pipeline.

The application uses FastAPI for the backend and Streamlit for the frontend, with vector-based semantic retrieval and an LLM for generating answers from uploaded documents.

---

## 🚀 Features

### 📄 Document Management

- Upload PDF, TXT, and DOCX documents
- Store uploaded documents
- View uploaded documents
- Delete documents
- Track document metadata

### 🔍 Semantic Retrieval

- Convert document content into chunks
- Generate vector embeddings
- Store embeddings in the vector store
- Perform semantic similarity search
- Retrieve relevant document chunks for questions

### 🤖 RAG-Based Question Answering

- Ask questions about uploaded documents
- Retrieve relevant context
- Generate answers using the retrieved context
- Prevent answers based on outside knowledge
- Return a fallback response when the answer is not available

### 📚 Source Attribution

Each answer can include information about the document and the chunks used to generate the answer.

Example:

```text
Answer:
Nvidia was founded by Jensen Huang, Chris Malachowsky, and Curtis Priem.

Source:
Nvidia.txt

Chunks:
0, 3, 7
```

### 💬 Chat Interface

The Streamlit frontend provides:

- Chat-style interface
- Question and answer history
- Markdown responses
- Numbered lists
- Bullet points
- Markdown tables
- Source information
- Backend connection status

---

# 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      Streamlit      │
                    │       Frontend      │
                    └──────────┬──────────┘
                               │
                               │ HTTP
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │       Backend       │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        Document API       Chat API        Health API
              │                │
              │                ▼
              │          ┌─────────────┐
              │          │ RAG Service │
              │          └──────┬──────┘
              │                 │
              │       ┌─────────┼─────────┐
              │       │         │         │
              │       ▼         ▼         ▼
              │  Retriever  Prompt     LLM
              │             Builder
              │       │
              │       ▼
              │  Vector Store
              │       │
              │       ▼
              │   Embeddings
              │
              ▼
        Document Storage
```

---

# 🔄 RAG Pipeline

DocuMind processes documents and questions through the following pipeline:

```text
Document Upload
       │
       ▼
Document Processing
       │
       ▼
Text Chunking
       │
       ▼
Embedding Generation
       │
       ▼
Vector Store
       │
       ▼
User Question
       │
       ▼
Query Embedding
       │
       ▼
Semantic Retrieval
       │
       ▼
Relevant Document Chunks
       │
       ▼
Context Construction
       │
       ▼
Prompt Builder
       │
       ▼
LLM
       │
       ▼
Answer + Sources
```

---

# 📁 Project Structure

```text
DocuMind/
│
├── backend/
│   ├── api/
│   │   ├── router.py
│   │   └── ...
│   ├── db/
│   │   ├── documind.db
│   │   └── ...
│   ├── embeddings/
│   │   └── ...
│   ├── generation/
│   │   ├── llm.py
│   │   └── prompt_builder.py
│   ├── prompts/
│   │   └── qa_prompt.txt
│   ├── retrieval/
│   │   ├── retriever.py
│   │   └── vector_store.py
│   ├── services/
│   │   ├── ingestion_service.py
│   │   └── rag_service.py
│   ├── tests/
│   │   └── ...
│   ├── config.py
│   └── main.py
│
├── frontend/
│   ├── components/
│   │   ├── chat.py
│   │   ├── delete_dialog.py
│   │   ├── document_table.py
│   │   ├── header.py
│   │   ├── sidebar.py
│   │   ├── system_status.py
│   │   └── upload.py
│   ├── services/
│   │   └── api_client.py
│   └── app.py
│
├── .gitignore
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🛠️ Technology Stack

| Technology     | Purpose                                 |
| -------------- | --------------------------------------- |
| Python         | Core programming language               |
| FastAPI        | Backend REST API                        |
| Streamlit      | Frontend application                    |
| LangChain Core | Document and LLM abstractions           |
| ChromaDB       | Vector storage and similarity retrieval |
| OpenAI         | Embeddings and LLM                      |
| SQLite         | Application database                    |
| Uvicorn        | FastAPI server                          |
| Requests       | Frontend API communication              |

---

# 🔐 Environment Variables

Create:

```text
backend/.env
```

Add:

```env
OPENAI_API_KEY=your_openai_api_key
```

Do not commit API keys or `.env` files to GitHub.

---

# ⚙️ Installation

## 1. Clone the repository

```powershell
git clone <your-repository-url>
cd DocuMind
```

## 2. Create a virtual environment

```powershell
python -m venv venv
```

## 3. Activate the virtual environment

```powershell
.env\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate:

```powershell
.env\Scripts\Activate.ps1
```

## 4. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# ▶️ Running the Application

DocuMind consists of a FastAPI backend and a Streamlit frontend.

## Start the Backend

From the project root:

```powershell
uvicorn backend.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Start the Frontend

Open another terminal and run:

```powershell
streamlit run frontend/app.py
```

---

# 📄 Uploading Documents

1. Open the Streamlit dashboard.
2. Select a document.
3. Supported formats:
   - PDF
   - TXT
   - DOCX
4. Click **Upload Document**.
5. The backend processes the document.
6. The document becomes available for question answering.

---

# 💬 Asking Questions

After uploading a document, ask questions through the chat interface.

Example:

```text
Who founded Nvidia?
```

Another example:

```text
What does CUDA do according to the document?
```

The system retrieves relevant document chunks and generates an answer from that context.

---

# 🧠 Grounded Question Answering

DocuMind is designed to answer questions using the uploaded document context.

The QA prompt instructs the model to:

- Answer only from the provided context
- Avoid outside knowledge
- Avoid hallucinating information
- Keep answers clear and concise
- Combine information when multiple chunks contribute to an answer

If the answer cannot be found in the retrieved context, the system returns:

```text
I don't know based on the uploaded documents.
```

Example:

```text
Question:
Who is the founder of Microsoft?

Answer:
I don't know based on the uploaded documents.
```

---

# 📚 Source Attribution

DocuMind returns source information along with answers.

Example:

```json
{
  "answer": "Nvidia announced to extend CUDA support to RISC-V on July 21, 2025.",
  "sources": [
    {
      "document_id": "document-id",
      "filename": "Nvidia.txt",
      "chunks": [49, 141, 144, 147, 150]
    }
  ]
}
```

This allows users to understand which uploaded document and chunks contributed to the answer.

---

# 🧪 Testing

Run the RAG service test:

```powershell
python -m backend.tests.test_rag_service
```

Other tests can be executed using their corresponding module names, for example:

```powershell
python -m backend.tests.test_embeddings
```

```powershell
python -m backend.tests.test_retriever
```

```powershell
python -m backend.tests.test_vector_store
```

```powershell
python -m backend.tests.test_prompt_builder
```

---

# 🔒 Git and Sensitive Files

The following should not be committed:

```text
.env
backend/.env
venv/
.venv/
backend/uploads/
backend/vector_store/
__pycache__/
*.py[cod]
```

API keys must always be stored in environment variables.

---

# 📊 Project Status

| Component           | Status      |
| ------------------- | ----------- |
| FastAPI Backend     | ✅ Complete |
| Streamlit Frontend  | ✅ Complete |
| Document Upload     | ✅ Complete |
| Document Listing    | ✅ Complete |
| Document Deletion   | ✅ Complete |
| Document Processing | ✅ Complete |
| Text Chunking       | ✅ Complete |
| Embeddings          | ✅ Complete |
| Vector Retrieval    | ✅ Complete |
| RAG Pipeline        | ✅ Complete |
| LLM Integration     | ✅ Complete |
| Source Attribution  | ✅ Complete |
| Grounded Fallback   | ✅ Complete |
| Chat Interface      | ✅ Complete |
| Markdown Responses  | ✅ Complete |
| Git Configuration   | ✅ Complete |

---

# 🚧 Future Improvements

Potential future improvements include:

- User authentication
- Persistent chat history
- Advanced document management
- Retrieval evaluation
- Reranking
- Production deployment
- Monitoring and logging
- Multi-user support

---

# 👨‍💻 Author

**Suraj Kumar Singh**

Computer Science & Engineering

---

# 📄 License

This project is intended for educational and portfolio purposes.
