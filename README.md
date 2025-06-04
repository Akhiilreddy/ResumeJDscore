# ResumeJDscore
# 🧠 AI-Powered Resume Search Engine

A Streamlit web app that finds the most relevant resumes from a set of PDFs using AI-powered semantic search. Paste a job description, and the app shows the top matching resumes based on their similarity.

---

## 🔍 Features

- Semantic resume search using sentence embeddings
- PDF text extraction using PyMuPDF
- Cosine similarity matching
- Match scores shown in percentages
- Upload additional resumes dynamically
- View resume content on click

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-search-engine.git
cd resume-search-engine

**### Folder Structure **

resume-search-engine/               <- 🔹 Main project folder (your GitHub repo name)
│
├── app.py                          <- Main Streamlit app
├── embedder.py                     <- Embedding logic
├── index_resumes.py                <- Resume indexing and search
├── resume_parser.py                <- PDF to text extraction
├── vector_store.py                 <- Cosine similarity vector store
│
├── resumes/                        <- Sample resumes (you can .gitignore this)
│   └── sample_resume1.pdf
│
├── requirements.txt                <- Python dependencies
├── README.md                       <- 📄 Most important file on GitHub!
├── .gitignore                      <- Ignore Python cache, virtual env, PDFs, etc.
