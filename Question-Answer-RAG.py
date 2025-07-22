import os
import streamlit as st
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Function: Load PDF and add page number metadata
def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    for i in range(len(pages)):
        pages[i].metadata['page_number'] = i + 1
    return pages

# Function: Split into chunks
def split_document(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    return splitter.split_documents(documents)

# Function: Create vector store
def create_vectorstore(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(chunks, embedding_model)

# Function: Get LLM (Groq)
def get_llm():
    return ChatGroq(api_key=groq_api_key, model_name="llama-3.3-70b-versatile")

# Function: Build QA chain
def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = get_llm()
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

# Function: Answer question and cite pages
def answer_question(qa_chain, query):
    result = qa_chain.invoke({"query": query})
    answer = result["result"]
    sources = result["source_documents"]

    cited_pages = []
    for doc in sources:
        page_number = doc.metadata.get("page_number", "N/A")
        if page_number not in cited_pages:
            cited_pages.append(page_number)
    cited_pages.sort()
    page_list = ", ".join(str(p) for p in cited_pages)

    return answer, page_list

# ---------------- Streamlit UI ---------------- #
st.set_page_config(page_title="📄 PDF-QA with Groq", layout="wide")
st.title("📄 AI-Powered PDF Q&A with Cited Pages")
st.markdown("Upload a PDF and ask anything about it. The AI will answer with page citations. 🤖")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file:
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())


    # User inputs a question
    query = st.text_input("Ask a question from the PDF:")

    if query:
        with st.spinner("Processing... please wait ⏳"):
            docs = load_pdf("temp.pdf")
            chunks = split_document(docs)
            vectorstore = create_vectorstore(chunks)
            qa_chain = build_qa_chain(vectorstore)
            answer, cited = answer_question(qa_chain, query)

        st.markdown(f"### 📌 Answer\n{answer}")
        st.markdown(f"**📄 Cited Pages:** {cited}")
