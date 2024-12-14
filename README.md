# Cold Mail Generator - RAG Application

## Overview
The **Cold Mail Generator** is a powerful Retrieval Augmented Generation (RAG) application that allows users to extract job-related information from URLs, process it using machine learning models, and generate personalized cold emails based on the data. This app leverages advanced natural language processing techniques to analyze job postings and match skills with relevant tech stacks stored in a personalized portfolio.

The app also includes functionality to add new tech stacks to the portfolio, updating both the database (CSV and ChromaDB) and enabling the generation of new cold emails based on the updated information.

### Key Features:
- **RAG (Retrieval Augmented Generation)**: Retrieves relevant tech stack data from the portfolio based on job skills and generates cold emails using LLM (Large Language Models).
- **Tech Stack Management**: Ability to add new tech stacks with corresponding links to the portfolio, which are both stored in a CSV file and in ChromaDB for easy querying.
- **Llama 3.1 Integration**: Utilizes the power of the Llama 3.1 model for text extraction, email generation, and job matching.
- **GroQ**: Optimizes and accelerates model inference, enhancing the performance of the app, especially for large-scale data processing.
  
## Tech Stack
- **Frontend**: Streamlit - For creating the interactive web interface.
- **Backend**: Python - The main application logic is written in Python, utilizing various libraries.
- **Machine Learning**:
  - **Llama 3.1** - For job information extraction and cold email generation.
  - **GroQ** - Used to optimize the LLM's performance for faster data processing and inference.
- **Data Storage**:
  - **CSV** - To store tech stacks and links.
  - **ChromaDB** - For persistent and scalable vector storage, enabling fast querying of tech stack data.
- **Libraries**:
  - `pandas` - For data manipulation (e.g., loading and updating CSV files).
  - `chromadb` - For managing the ChromaDB client and collections.
  - `uuid` - For generating unique identifiers.
  - `streamlit` - For building the web application interface.
  - `langchain_community.document_loaders` - For web scraping job postings.

## Installation

### Prerequisites
- Python 3.x
- `pip` or `conda` (for installing dependencies)

### Steps to Run the Project Locally:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cold-mail-generator.git
   cd cold-mail-generator
