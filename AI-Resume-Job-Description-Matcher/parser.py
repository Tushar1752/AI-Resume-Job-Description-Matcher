import PyPDF2
from docx import Document


def extract_pdf(file):
    text = ""

    pdf = PyPDF2.PdfReader(file)

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_docx(file):
    doc = Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text