import pdfplumber
import docx


class ResumeParser:

    def extract_pdf_text(self, file):

        text = ""

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    def extract_docx_text(self, file):

        document = docx.Document(file)

        text = ""

        for para in document.paragraphs:

            text += para.text + "\n"

        return text

    def extract_text(self, uploaded_file):

        filename = uploaded_file.name.lower()

        if filename.endswith(".pdf"):

            return self.extract_pdf_text(uploaded_file)

        elif filename.endswith(".docx"):

            return self.extract_docx_text(uploaded_file)

        else:

            return "Unsupported File Format"