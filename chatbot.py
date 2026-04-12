from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm(model_name: str, temperature: float = 0.7):
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name=model_name,
        temperature=temperature,
    )


def build_chain(model_name: str, temperature: float = 0.7):
    llm = get_llm(model_name, temperature)
    memory = ConversationBufferMemory(return_messages=True)
    chain = ConversationChain(llm=llm, memory=memory, verbose=False)
    return chain


def chat(chain: ConversationChain, user_input: str) -> str:
    response = chain.predict(input=user_input)
    return response
