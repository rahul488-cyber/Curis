import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, PDFSearchTool, WebsiteSearchTool
from .vision_tool import ImageQandATool

import keys


os.environ["SERPER_API_KEY"] =  keys.SERPER_API_KEY
# os.environ["OPENAI_API_KEY"] =  userdata.get('OpenAI-API-Key')


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
injured_image_q_and_a = ImageQandATool()