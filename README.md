# Customer Support Chatbot (PDF-based)

This is a smart AI chatbot that answers customer queries using your uploaded business documents (PDF or text). It uses advanced AI models to retrieve accurate answers based on the content.

## Features

- Upload PDFs or text files
- Ask questions in natural language
- Automatically finds the most relevant answers from the uploaded content
- Real-time chatbot experience

## Tech Stack

- **LangChain**
- **FAISS** (Vector Store)
- **SentenceTransformers** (Embeddings)
- **Streamlit** (Frontend UI)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Imdad990/Cudtomer_Support_Chatbot.git
cd Cudtomer_Support_Chatbot
Install the required packages:

bash
Copy
Edit
pip install -r requirement.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Then, open your browser and go to http://localhost:8502

Project Files
File Name	Description
app.py	Main Streamlit application
chunks.pkl	Saved text chunks from documents
faiss_index.index	FAISS index for fast retrieval
requirement.txt	Required Python libraries
How It Works
Upload a PDF or text file.

The content is split into small chunks.

Each chunk is converted to a vector using Sentence Transformers.

FAISS indexes these vectors for fast similarity search.

When a question is asked, it is also embedded and matched against the chunks.

The most relevant answer is displayed.

Use Cases
Customer support for product manuals

Chatbot for internal documentation

HR document assistance

Educational material Q&A

License
This project is open-source and free to use under the MIT License.

Created by Imdad Ullah Khan









