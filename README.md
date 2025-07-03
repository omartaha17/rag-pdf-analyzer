# AI PDF Analyzer

A Streamlit app that lets you upload a PDF and ask questions about its content using OpenAI embeddings and GPT-4. It performs document chunking, similarity matching, and returns intelligent answers based on the most relevant sections.

---

## Features

-  Upload any PDF file
-  Automatically extracts and chunks the text
-  Embeds chunks using `text-embedding-3-small` model
-  Compares your question to the document using cosine similarity
-  Uses GPT-4 to answer your question based on top-matching chunks
-  Clean and responsive Streamlit UI

---

##  Demo


---
## Tech Stack

Python

Streamlit

PyMuPDF (fitz)

OpenAI API (Embeddings + Chat)

NumPy


## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/TegeTiger/rag-pdf-analyzer
cd rag-pdf-analyzer
