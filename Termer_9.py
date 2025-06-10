!pip install langchain langchain-core langchain-community cohere pydantic wikipedia-api

from langchain_community.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel
import wikipediaapi

class InstitutionDetails(BaseModel):
    founder: str
    founded: str
    branches: str
    employees: str
    summary: str

def fetch_wikipedia_summary(institution_name, max_chars=3000):
    wiki = wikipediaapi.Wikipedia(language='en', user_agent='InstitutionInfoBot/1.0 (https://www.wikipedia.org/)')

    page = wiki.page(institution_name)
    if not page.exists():
        return "No information available."
    return page.text[:max_chars]

prompt_template = """
Extract the following information from the given text:
- Founder
- Founded (year)
- Current branches
- Number of employees
- 4-line brief summary

Text: {text}

Format:
Founder: <founder>
Founded: <founded>
Branches: <branches>
Employees: <employees>
Summary: <summary>
"""

if __name__ == "__main__":
    institution_name = input("Enter the name of the institution: ")
    wiki_text = fetch_wikipedia_summary(institution_name)

    llm = Cohere(cohere_api_key="CVGjIIPbmzyRKxVm3GNhxPresBQuS3WH0QVIuK8o")

    prompt = PromptTemplate.from_template(prompt_template)
    chain = prompt | llm  
    
    response = chain.invoke({"text": wiki_text})

    try:
        lines = response.strip().split('\n')
        info = {line.split(':')[0].lower(): ':'.join(line.split(':')[1:]).strip() for line in lines if ':' in line}
        details = InstitutionDetails(
            founder=info.get("founder", "N/A"),
            founded=info.get("founded", "N/A"),
            branches=info.get("branches", "N/A"),
            employees=info.get("employees", "N/A"),
            summary=info.get("summary", "N/A")
        )
        print("\nInstitution Details:")
        print(f"Founder: {details.founder}")
        print(f"Founded: {details.founded}")
        print(f"Branches: {details.branches}")
        print(f"Employees: {details.employees}")
        print(f"Summary: {details.summary}")
    except Exception as e:
        print("Error parsing response:", e)
