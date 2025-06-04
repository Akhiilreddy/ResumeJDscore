import os
from resume_parser import extract_text_from_pdf
from embedder import get_embedding
from vector_store import ResumeVectorStore

store = ResumeVectorStore()

folder = "resumes"
for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(os.path.join(folder, filename))
        embedding = get_embedding(text)
        store.add(embedding, {"filename": filename, "text": text})

store.build_index()
