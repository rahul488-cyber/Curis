import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.environ["SERPER_API_KEY"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# print(
#     SERPER_API_KEY,
#     GEMINI_API_KEY,
#     OPENAI_API_KEY
# )