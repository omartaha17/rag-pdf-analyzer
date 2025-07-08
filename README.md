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

![App Demo 1](ragpdemo3.png)
---
## Tech Stack

Python

Streamlit

PyMuPDF (fitz)

OpenAI API (Embeddings + Chat)

NumPy


## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/TegeTiger/rag-pdf-analyzer
cd rag-pdf-analyzer

2. Create a virtual environment and activate it
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your `.env` file
```
OPENAI_API_KEY=your_real_key
```

5. Run the app
```bash
streamlit run app.py
```

---

## Author

Built by Omar Taha  
Connect on [LinkedIn](https://www.linkedin.com/in/omar-taha-133840269/) or [GitHub](https://github.com/TegeTiger)

