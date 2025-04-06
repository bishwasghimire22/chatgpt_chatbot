# PDF Chatbot with OpenAI GPT-3.5 and Streamlit

A chatbot that can read and answer questions based on a PDF file using OpenAI's GPT-3.5 model. The app leverages Langchain for handling the QA chain and FAISS for efficient vector-based search.

## Features

- **PDF Upload**: Upload a PDF document to the chatbot.
- **Text Extraction**: Extracts text from the PDF.
- **Vector Search**: Uses OpenAI embeddings and FAISS for semantic search.
- **Question Answering**: Ask questions and get relevant answers based on the content of the PDF.

## Requirements

- Python 3.8+
- Streamlit
- OpenAI API key

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-chatbot.git
   cd pdf-chatbot
   ```
2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. Create a .env file in the root directory and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your-openai-api-key-here
   ```
4. Run the Sreamlit app:
   ```bash
   streamlit run app.py
   ```
