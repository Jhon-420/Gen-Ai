!pip install langchain cohere

from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain import LLMChain
from google.colab import drive

drive.mount('/content/drive')

file_path = "/content/drive/MyDrive/8thsample_text.txt" 
with open(file_path, "r") as file:
    text = file.read()

cohere_api_key = "CVGjIIPbmzyRKxVm3GNhxPresBQuS3WH0QVIuK8o" 
prompt_template = """
Summarize the following text in three bullet points:
{text}
"""

llm = Cohere(cohere_api_key=cohere_api_key)
prompt = PromptTemplate(input_variables=["text"], template=prompt_template)
chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(text)

print("Summarized Output in Bullet Points:")
print(result)
