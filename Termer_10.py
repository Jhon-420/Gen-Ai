!pip install langchain cohere faiss-cpu kagglehub pandas

# api_key = "CVGjIIPbmzyRKxVm3GNhxPresBQuS3WH0QVIuK8o"

import os
import kagglehub
import pandas as pd
from langchain_community.llms import Cohere
from langchain.vectorstores import FAISS
from langchain.embeddings import CohereEmbeddings
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

cohere_api_key = input("Enter your Cohere API key: ").strip()

dataset_path = kagglehub.dataset_download("dev523/indian-penal-code-ipc-sections-information")
print("Downloaded dataset at:", dataset_path)

csv_file = os.path.join(dataset_path, "ipc_sections.csv")
df = pd.read_csv(csv_file)

documents = []
for _, row in df.iterrows():
    section_text = f"Section: {row.get('Section', '')}\nTitle: {row.get('Title', '')}\nDescription: {row.get('Description', '')}"
    documents.append(Document(page_content=section_text))

embeddings = CohereEmbeddings(
    cohere_api_key=cohere_api_key,
    user_agent="ipc_qa_bot/1.0"
)

vectorstore = FAISS.from_documents(documents, embeddings)

llm = Cohere(cohere_api_key=cohere_api_key, model="command")

qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

print("\nAsk questions about the Indian Penal Code (type 'exit' to quit):")
while True:
    query = input("Question: ")
    if query.lower() == "exit":
        print("Goodbye!")
        break
    response = qa_chain.run(query)
    print(f"Answer: {response}\n")
