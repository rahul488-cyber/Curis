from crewai import Task
from pydantic import BaseModel

class MedicineChose(BaseModel):
    medicine_chose: str

def injury_analyzing_task(agent):
    return Task(
            description=(
                "Using the detailed description about the description of the image having the open-wound or burn injury "
                "Generate a Well structured Document "
                "That clearly explains and gives insights about the injury "
                """Injury Description and other detail: 
                    Patient's Name: {patients_name}
                    Patient's Age: {patients_age}
                    Pateint's Gender: {patients_gender}
                    description of the image of injury: {injury_desc_from_image} 
                    source of injury(how did the injury happen): {source_of_injury}
                    pain-level out of 10: {pain_level}
                    prior medical conditions: {prior_medical_conditions}
                    additional-description: {addition_desc}
                """
                "use the image q&a tool and get more insights from the image if necessary "
                "utilize web search and scape tool to get more information. "
                "Make sure everything is explained in-detail as it would be helpful for other agents to understand"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            agent = agent,
            allow_delegation=False,
            async_execution=True # Will be executed asynchronously
            )


def medicine_analyzing_task(agent):
    # to make a structured write-up
    return Task(
            description=(
                "The task is to analyse the given medicines below and give out the descriptions and insights of what they do "
                "where they are used in what cases(i.e their use-cases), their side-effects and their pros and description."
                "Medicines Available: {medicine_list} "
                "utilize web search and scape tool to get detailed and latest information about these meds. "
                "Make sure everything is explained in-detail as it would be helpful for other agents to understand"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            agent = agent,
            allow_delegation=False,
            async_execution=True # Will be executed asynchronously
        )


def injury_report(agent, context):
    # to make a structured write-up
    return Task(
            description=(
                "Using the detailed description about the injury and the patient "
                "Generate a Well structured MarkDown Document "
                "The heading should be the 'Injury Report - {patients_name}' "
                "the subheadings should be related to "
                "1. Patient's details. "
                "2. Overall summary of the Injury. "
                "3. What type of injury it is. "
                "4. Explanation of how the injruy happened. "
                "5. Additional details related to the injury if any. "
                "utilize web search and scape tool to get more information and structure for the document."
            ),
            expected_output = (
                "A Mardown document clearly explaining aspects given in the description."
            ),
            context=context,
            agent = agent,
            allow_delegation=False
        )


def injury_report_checker(agent, context):
    return Task(
            description=(
                "Using the document fed or got from the previous agent, your "
                "task is to go through the report and make changes if any needed and improvise its quality as well"
                "if you feel its not good enough you can delegate the work back and get a better one as well"
                "utilize web search and scape tool to get more information and structure for improvising the document."
            ),
            expected_output = (
                "A Mardown document clearly explaining aspects given in the description. Make sure only markdown output is given. no other explanation's necessary"
            ),
            context=context,
            agent = agent,
            allow_delegation=False,
            output_file='injury-report-analysis.md'
        )


def medicine_report(agent, context):
    return Task(
            description=(
                "Using the detailed description about the medicines available to treat the patient "
                "Generate a Well structured MarkDown Document "
                "The heading should be the 'Medical Stock Report' "
                "every single medicines name should be listed "
                "under them the subheadings for each medicine should be related to "
                "1. a short description about the medicine. "
                "2. what is the medicine made of. "
                "3. in what case is the medicine used to treat. "
                "4. side-effects of the medicine "
                "utilize web search and scape tool to get more information and structure for the document."
            ),
            expected_output = (
                "A Mardown document clearly explaining aspects given in the description."
            ),
            context=context,
            agent = agent,
            allow_delegation=False
        )


def medicine_report_checker(agent, context):
    return Task(
        description=(
            "Using the document fed or got from the previous agent, your "
            "task is to go through the report and make changes if any needed and improvise its quality as well"
            "utilize web search and scape tool to get more information and structure for improvising the document."
        ),
        expected_output = (
            "A Mardown document clearly explaining aspects given in the description. Make sure only markdown output is given. no other explanation's necessary"
        ),
        context= context,
        agent = agent,
        allow_delegation=False,
        output_file='medicine-report-analysis.md'
        )


def treating_task(agent, context):
    return Task(
            description=(
                "Using the detailed description about the description of injury and avaiable medicines "
                "Your task is to choose the appropriate medicine based on the injury to treat the patient "
                "utilize web search and scape tool to get more information to make the right description "
                "and explain the reason behind choosing the medicine to treat the patients wound "
                "Make sure everything is explained in-detail as it would be helpful for other agents to understand"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            context= context,
            agent = agent,
            allow_delegation=False,
        )


def treatment_report(agent, context):
    return Task(
            description=(
                "Using the detailed description about the treatment given by previous agent "
                "Generate a Well structured MarkDown Document "
                "The heading should be the 'Diagnosis and Treatment - Report' "
                "You should give a breif description about the whole process. "
                "You should have sub-headings clearly describing which medicine was chose and why was it chosen. "
                "And give other important details like healing time and more. "
                "utilize web search and scape tool to get more information and structure for the document."
            ),
            expected_output = (
                "A Mardown document clearly explaining aspects given in the description."
            ),
            context= context,
            agent = agent,
            allow_delegation=False
        )


def treatment_report_checker(agent, context):
    return Task(
            description=(
                "Using the document fed or got from the previous agent, your "
                "task is to go through the report and make changes if any needed and improvise its quality as well "
                "utilize web search and scape tool to get more information and structure for improvising the document. "
                
            ),
            expected_output = (
                "A Mardown document clearly explaining aspects given in the description. Make sure only markdown output is given. no other explanation's necessary"
            ),
            context= context,
            agent = agent,
            allow_delegation=False,
            output_file="treatment_report.md"
        )


def medicine_chose(agent, context):
    return Task(
    description=(
        "Using the detailed description about the treatment given by previous agent "
        "Choose a medicine out of the following medicines {medicine_list}"
        
    ),
    expected_output = (
        "A json file containing a key which holds a medicine chose for treating the patient from the list of medicines {medicine_list}"
    ),
    context=context,
    agent = agent,
    tools = [], # purposefully left it empty
    allow_delegation=False,
    output_json=MedicineChose,
    output_file="medicine_chose.json"
)