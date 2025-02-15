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

# Prompt Templates

A PromptTemplate in LangChain is a structured way to format prompts dynamically. It allows you to define a prompt with placeholders and then fill in those placeholders with actual values at runtime. This helps in creating reusable and consistent prompts for LLM interactions.

There is one limitation with this, whenever we create a prompt template and give it values, it is always a list with one humanMessage. What if we want more control? like customising the SystemMessage too.
For that we can have a list of tuples.(refer to code)

# Chains

Chains are sequences of modular components (like LLMs, prompt templates, memory, and tools) that work together to process and generate responses. Instead of handling each step separately, Chains automate the flow of data through these components.

## Types of Chaining

1. ParallelChain – Lets tasks run independently without being dependent on each other.
2. SequentialChain – Chains multiple steps together in sequence.
3. RouterChain / ConditionalChaining – Routes inputs to different sub-chains based on conditions.
4. AgentChain – Uses AI agents to decide which tools or actions to use.
