# LANGCHAIN

Langchain core components
1. Chat models
2. Prompt templates
3. Chains
4. RAGs
5. Agents and tools

For using langchain, first we create a virtual environment.

```python
python3 -m venv .venv
```

## Chat Models
Chat models is a component designed to communicate in a structured way with LLMs like GPT-4, Hugging Face and Claude Sonnet.

Why use langchain chat models? 

1. Consistent Workflow
2. Easy switching between LLMs
3. Context management
4. Efficient chaining
5. Scalability

```
pip3 install -qU langchain-openai
```

this will install langchain for openAI.

## Types of Messages in Langchain

1. System Message: Defines the AI's role and sets the context for the conversation. Eg: 'Youa re a marketing agent.'
2. Human Message: Represents user input or questions directe towards AI.
3. AI Message: Contains the AI response based on previous messages.

We don't want to store messages locally, we can get a db and satore messages there like firebase.
(Storing mesages to the cloud.)