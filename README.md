# 🧠 Agentic Retrieval-Augmented Generation (RAG) Projects

Welcome to the **SaumyaShah09 / Agentic-RAG** repository — a collection of practical and advanced RAG-based notebooks and utilities for enhancing AI reasoning, search, and summarization using LLMs.

---

## 📚 Overview

This repo contains multiple **RAG (Retrieval-Augmented Generation)** pipelines that explore various techniques like:

- 🧠 Query Expansion with Generated Answers
- 🌐 Website Scraping + Q&A
- 💬 Question Answering on Document Chunks
- 🔄 Agentic RAG Workflows
- ⚙️ LangSmith-based Debugging for RAG
- 📑 PDF Summarization and Embedding

Each notebook demonstrates a real-world use case of **LLMs + RAG**, enhanced by utilities and prompt engineering.

---

## 📂 Notebooks Included

| Notebook Name                                             | Description                                                                 |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| `Agentic-RAG.ipynb`                                       | Agent-based reasoning using RAG + multi-step tasks                         |
| `Query-expansion-with-generated-answer-RAG.ipynb`         | Improves retrieval by expanding queries using LLM-generated context        |
| `Question-Answer-RAG.ipynb`                               | Basic implementation of RAG for answering user questions                   |
| `RAG-using-Langsmith.ipynb`                               | Integrates [LangSmith](https://www.langchain.com/langsmith) for RAG debugging |
| `Website-scraper-Q&A.ipynb`                               | Scrapes websites and uses RAG for answering based on scraped content       |
| `multiple-queries.ipynb`                                  | Combines multiple queries and results for robust QA                        |

---

## 🛠️ Other Files

| File Name                    | Purpose                                                    |
|-----------------------------|------------------------------------------------------------|
| `helper_utils.py`           | Utility functions used in the notebooks                    |
| `artificial_intelligence.pdf` | Source PDF used for RAG testing and summarization         |
| `genai-principles.pdf`      | Another test document used for extracting answers          |
| `extracted_blogs.zip`       | Pre-downloaded blog content for QA experiments             |

---

## 🔧 Tech Stack

- **Python 3.10+**
- **LangChain**
- **OpenAI / Groq / HuggingFace LLMs**
- **FAISS / Chroma for Vector DB**
- **BeautifulSoup / Requests (for scraping)**
- **LangSmith (optional debugging & tracing)**

---

## 🚀 Quick Start

```bash
git clone https://github.com/SaumyaShah09/Agentic-RAG
cd Agentic-RAG
pip install -r requirements.txt  # Make sure you have langchain, openai, bs4, etc.
