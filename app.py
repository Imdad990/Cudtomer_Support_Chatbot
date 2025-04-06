# Save this as app.py

import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load existing FAISS index and model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load saved index and chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

index = faiss.read_index("faiss_index.index")

def get_answer(query, top_k=1):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    result = [chunks[i] for i in indices[0]]
    return result[0]

st.title("Imdad Retrieval-based PDF Chatbot")

query = st.text_input("Ask a question:")

if query:
    answer = get_answer(query)
    st.markdown("### 💬 Chatbot Answer")
    st.write(answer)
