
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.

genai.configure(api_key='AIzaSyDBtuGMgyUCmAegeXZkBjf6ey-L8MdBCwk')
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)


model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("はじめまして")
print(response.text)