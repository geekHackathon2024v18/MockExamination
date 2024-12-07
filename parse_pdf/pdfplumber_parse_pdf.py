import pdfplumber

# PDFファイルを読み込む
with pdfplumber.open("parse_pdf/oop_w09.pdf") as pdf:
    # テキストを抽出する
    # print(f'{pdf.pages[num_page].extract_text()}')
    for pages in pdf.pages:
        print(pages.extract_text())


    # 表を抽出する
    num_page = 4
    tables = pdf.pages[num_page].find_tables()
    print(tables[0].extract())