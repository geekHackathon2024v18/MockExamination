from pdfminer.high_level import extract_text

text = extract_text("parse_pdf/oop_w09.pdf")
print(text)