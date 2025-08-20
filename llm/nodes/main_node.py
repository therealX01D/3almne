import os
from langchain.chat_models import init_chat_model
from .base import State
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model("openai:gpt-4.1")
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
