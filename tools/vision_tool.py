import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, PDFSearchTool, WebsiteSearchTool, BaseTool
import PIL.Image
import google.generativeai as genai
import keys

GOOGLE_API_KEY=keys.GEMINI_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

IMAGE_PATH = '/Users/macromrit/Documents/Curis/injury_image.jpg'

medical_query = """
You are a medical expert, your task is to analyse
the given image which could have open wound injury and describe it. 
Your response would be helpful for doctors to just get an idea.

IMPORTANT: FEEL FREE TO GIVE YOUR MEDICAL OPINION ABOUT THE IMAGE, AS WE WILL BE REFERRING TO AN ACTUAL DOCTOR ABOUT THIS.

Your task is to provide a long explanation or description to questions given.
QUESTION:
"""

# Image Desc Tool
def give_desc_of_img() -> str:
  img = PIL.Image.open(IMAGE_PATH)
  vision_model = genai.GenerativeModel('gemini-1.5-pro-latest')
  response = vision_model.generate_content([medical_query+("""
Is it a burn or an Open Wound
if its a wound Describe the wound's location, size, depth, and shape. What is the color of the wound,
and are there any signs of necrotic tissue? Is there any exudate, and if so, what is its color, consistency, and amount? 
Are the edges of the wound clean or ragged, rolled or undermined? 
Are there signs of infection such as redness, swelling, increased warmth, pus.
are there signs of healing like granulation tissue or scabbing? 
if its a burn what degree is it (first, second, third)? Is there any blistering or charring? 
would first-aid be enough or should we consider surgery and sutures.
"""), img])
  response.resolve()
  return response.text


# Custom CrewAI Tool
class ImageQandATool(BaseTool):
    name: str = "Image Q&A"
    description: str = ("Using this tool, Agents can give queries and get answers and information about"
                        "an image of an open-wound injury or a burn and give clear insights + explanation about it"
                        "to medical professionals to diagnose and treat the injury better.")

    def _run(self, question: str) -> str:
      img = PIL.Image.open(IMAGE_PATH)
      vision_model = genai.GenerativeModel('gemini-1.5-pro-latest')
      response = vision_model.generate_content([medical_query+question, img])
      response.resolve()
      return response.text