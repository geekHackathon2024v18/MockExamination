import pdfplumber

class PdfPlumberParsePdf:
    def __init__(self, file_name):
        self.file_name = file_name
        self.pdf = pdfplumber.open(self.file_name)

    def extract_text(self):
        text = ""
        for page in self.pdf.pages:
            text += page.extract_text() + "\n\n"
        return text

    def close(self):
        self.pdf.close()
