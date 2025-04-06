import PyPDF2
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


def extract_text_from_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += (
                page.extract_text() or ""
            )  # Ensure None values don't break the process
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
