from pypdf import PdfReader
from fastapi import UploadFile


def parse_pdf(file: UploadFile) -> str:
    reader = PdfReader(file.file)

    result = ''
    for page in reader.pages:
        result += page.extract_text()

    return result
