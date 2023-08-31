from pathlib import Path
import logging

import PyPDF2
import docx


LOGGER = logging.getLogger(__name__)


class FileReader:
    def __init__(self, path):
        LOGGER.debug(f"{self.__class__.__name__}.__init__()")
        self.path = Path(path)
        self.ext = self.path.suffix

    def _extract_text_from_pdf(self):
        LOGGER.debug(f"{self.__class__.__name__}._extract_text_from_pdf()")
        with open(self.path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = [page.extract_text() for page in reader.pages]
        return "\n".join(text)

    def _extract_text_from_docx(self):
        LOGGER.debug(f"{self.__class__.__name__}._extract_text_from_docx()")
        doc = docx.Document(self.path)
        text = [para.text for para in doc.paragraphs]
        return "\n".join(text)

    def _extract_text_from_txt(self):
        LOGGER.debug(f"{self.__class__.__name__}._extract_text_from_txt()")
        with open(self.path, "r") as f:
            return f.read()

    def extract_text(self):
        LOGGER.debug(f"{self.__class__.__name__}.extract_text()")
        print(self.ext)
        if self.ext == ".pdf":
            return self._extract_text_from_pdf()
        elif self.ext == ".docx":
            return self._extract_text_from_docx()
        elif self.ext == ".txt":
            return self._extract_text_from_txt()
        else:
            raise ValueError(f"File extension must be in ['.pdf', '.docx', '.txt']")
