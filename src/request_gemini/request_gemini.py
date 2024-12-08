
import textwrap
from parse_pdf.pdfplumber_parse_pdf import PdfPlumberParsePdf
import json

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from request_gemini import env

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.

def request_gemini():

  genai.configure(api_key=env.getApiKye())
  # for m in genai.list_models():
  #   if 'generateContent' in m.supported_generation_methods:
  #     print(m.name)


  # pdfのテキスト化
  pdf_parser = PdfPlumberParsePdf('parse_pdf/network_w09.pdf')
  pdf_text = pdf_parser.extract_text()

  model = genai.GenerativeModel('gemini-1.5-flash')
  # response = model.generate_content("はじめまして")
  # print(response.text)

  prompt = """授業の模擬的なテスト問題をjson形式で生成してもらいたいです。
  次の文章は、pdfをパースしてテキスト化したものです
  ```
  """
  prompt +=  pdf_text + "\n```\n"



  prompt += """
  これらの内容から、3~10問程度、問題文と選択式で候補の4択、その回答を出力してもらいたいです。
  Use this JSON schema:

  mock_examination = {'mock_examination_name': str, 'question_list': list[question]}
  question = {'question_sentence': str, 'choice_1: str, 'choice_2': str, 'choice_3': str, 'choice_4': str, answer': str}
  Return: mock_examination"""
  # print(prompt)
  result = model.generate_content(prompt)
  # print(result.text)
  json_data = result.text.replace('```json', '').replace('```', '')
  # print(json_data)
  data = json.loads(json_data)
  # for i in data['question_list']:
  #   print(f'問題文:{i['question_sentence']},  選択肢[1: {i['choice_1']}, 2: {i['choice_2']}, 3: {i['choice_3']}, 4: {i['choice_4']}], 答え: {i['answer']}')

  return data
