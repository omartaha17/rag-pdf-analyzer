import streamlit as st
import fitz
from dotenv import load_dotenv
import os
from openai import OpenAI
from funcs import split_into_chunks,calculate_cosine_similarity_numpy,mergesort

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI PDF Analyser", layout="centered")

uploaded_data = st.file_uploader("Upload a PDF", type="pdf")


if uploaded_data is not None:
    doc = fitz.open(stream=uploaded_data.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    chunks = split_into_chunks(text)

    client = OpenAI(api_key=OPENAI_API_KEY)

    chunk_response = client.embeddings.create(
        input=chunks,
        model="text-embedding-3-small"
    )

    chunk_embeddings = []
    for item in chunk_response.data:
        chunk_embeddings.append(item.embedding)

    embed_dict = dict(zip(chunks, chunk_embeddings))

    query = st.text_input("Ask a question about the document:")

    if query:
        query_response = client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        )
        query_embedding = query_response.data[0].embedding

        scores = []
        for chunk, emb in embed_dict.items():
            score = calculate_cosine_similarity_numpy(query_embedding, emb)
            scores.append((chunk, score))

        sortedscores = mergesort(scores)
        top_chunks = sortedscores[:3]
        response = "\n\n".join([chunk for chunk, score in top_chunks])

        completion_response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on PDF content."},
                {"role": "user", "content": f"The document contains:\n{response}\n\nMy question is: {query}"}
            ]
        )
        st.subheader("Answer")
        st.write(completion_response.choices[0].message.content)

