import pdfplumber

# PDFファイルを読み込む
with pdfplumber.open("parse_pdf/oop_w09.pdf") as pdf:
    # テキストを抽出する
    # print(f'{pdf.pages[num_page].extract_text()}')
    s = ""
    for pages in pdf.pages:
        s += pages.extract_text() + "\n\n"
        # print(pages.extract_text())
    print(s)
