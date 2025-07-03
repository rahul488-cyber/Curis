import os
from langchain_openai import ChatOpenAI
from keys import OPENAI_API_KEY, GEMINI_API_KEY
from tools.vision_tool import give_desc_of_img
from crewai import Crew
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
# from langchain_groq import ChatGroq



from tools.tool_kit import (
    search_tool,
    scrape_tool,
    injured_image_q_and_a
)

from agents import (
    medical_injury_analyzer, 
    clinical_pharmacologist,
    decision_and_report_quality_administrator,
    medical_report_writing_general_practitioner,
    primary_care_physician
)

from tasks import (
    injury_analyzing_task,
    medicine_analyzing_task,
    injury_report,
    injury_report_checker,
    medicine_report,
    medicine_report_checker,
    treating_task,
    treatment_report,
    treatment_report_checker,
    medicine_chose
)

# os.environ["OPENAI_API_KEY"] =  OPENAI_API_KEY

# llm = ChatOpenAI(model="gpt-4-turbo")
# llm = ChatOpenAI(model="gpt-4o")

# llama_3_name = "llama3-70b-8192"

# llm = ChatGroq(groq_api_key="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", 
#                model_name=llama_3_name)

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY, safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },)




agent_1 = medical_injury_analyzer(llm, [search_tool, injured_image_q_and_a]) # scrape_tool, 
agent_2 = clinical_pharmacologist(llm, [search_tool]) # scrape_tool, 
agent_3 = decision_and_report_quality_administrator(llm, [search_tool]) # scrape_tool,
agent_4 = medical_report_writing_general_practitioner(llm, [search_tool]) # scrape_tool,
agent_5 = primary_care_physician(llm, [search_tool]) # scrape_tool,

task_1 = injury_analyzing_task(agent_1)
task_2 = medicine_analyzing_task(agent_2)
task_3 = injury_report(agent_4, [task_1])
task_4 = injury_report_checker(agent_3, [task_3])
task_5 = medicine_report(agent_4, [task_2])
task_6 = medicine_report_checker(agent_3, [task_5])
task_7 = treating_task(agent_5, [task_4, task_6]) 
task_8 = treatment_report(agent_4, [task_7])
task_9 = treatment_report_checker(agent_3, [task_8])
task_10 = medicine_chose(agent_4, [task_7])


# Formulating the Crew
injury_management_crew = Crew(
    agents=[agent_1,
            agent_2,
            agent_3,
            agent_4,
            agent_5
            ],  

    tasks=[task_1,
           task_2,
           task_3,
           task_4,
           task_5,
           task_6,
           task_7,
           task_8,
           task_9,
           task_10], 
    verbose=True,
    memory=False
)


# Kicking off the crew

def kick_off_the_crew(
   patients_name: str,
   patients_age: int,
   patients_gender: str,
   source_of_injury: str,
   pain_level: int,
  prior_medical_conditions: str,
  addition_desc: str,
  medicine_list: list
):

    medical_details = {
                        'patients_name': patients_name,
                        'patients_age': str(patients_age),
                        'patients_gender': patients_gender,
                        'injury_desc_from_image': give_desc_of_img(),
                        'source_of_injury' : source_of_injury,
                        'pain_level': str(pain_level),
                        'prior_medical_conditions': prior_medical_conditions,
                        'addition_desc': addition_desc,
                        'medicine_list': str(medicine_list)
                    }

    return injury_management_crew.kickoff(inputs=medical_details)


if __name__ == "__main__":
    kick_off_the_crew(
        "marcus andrews",
        24,
        'Male',
        "fell down while Playing Soccer",
        '6',
        "None",
        "This injury happened just hours ago",
        ["Betadine", "Flamazine"]
    )
    # print(give_desc_of_img())