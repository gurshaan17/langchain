from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

messages = [
    SystemMessage("You are an expert in content strategy"),
    HumanMessage("Give a short tip to create engaging post on instagram")
]

llm = ChatOpenAI(model="gpt-4")
result = llm.invoke(messages)
print(result.content)