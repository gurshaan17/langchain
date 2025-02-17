from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

result = llm.invoke("What is the hex code of red?")

print(result.content)