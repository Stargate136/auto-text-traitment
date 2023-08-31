from pathlib import Path

import PyPDF2
import docx


class FileReader:
    def __init__(self, path):
        self.path = Path(path)
        self.ext = self.path.suffix

    def _extract_text_from_pdf(self):
        with open(self.path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = [page.extract_text() for page in reader.pages]
        return "\n".join(text)

    def _extract_text_from_docx(self):
        doc = docx.Document(self.path)
        text = [para.text for para in doc.paragraphs]
        return "\n".join(text)

    def _extract_text_from_txt(self):
        with open(self.path, "r") as f:
            return f.read()

    def extract_text(self):
        print(self.ext)
        if self.ext == ".pdf":
            return self._extract_text_from_pdf()
        elif self.ext == ".docx":
            return self._extract_text_from_docx()
        elif self.ext == ".txt":
            return self._extract_text_from_txt()
        else:
            raise ValueError(f"File extension must be in ['.pdf', '.docx', '.txt']")
