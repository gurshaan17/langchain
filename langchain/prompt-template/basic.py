from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

template = "Write a {tone} email to {company} expressing interest in {position} position, mentioning {skill} as a key strength. Keep the message small and upto 3 lines maximum."

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone": "energetic",
    "company": "apple",
    "position": "Engineer",
    "skill": "AI"
})

print(prompt)
print(llm.invoke(prompt).content)

messages2 = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template2 = ChatPromptTemplate.from_messages(messages2)
prompt2 = prompt_template2.invoke({"topic": "lawyers", "joke_count": 3})
print(prompt2)
result = llm.invoke(prompt2)
print(result.content)