import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key="YOUR API KEY",
    model_name="llama-3.1-8b-instant"
)

#state

class State(TypedDict):
    message : str


#chatbot Node

def chatbot(state):
    reply = llm.invoke(state["message"])
    return {"message": reply.content}


#langgraph

graph = StateGraph(State)

graph.add_node("chatbot", chatbot)

graph.set_entry_point("chatbot")

graph.add_edge("chatbot", END)

app = graph.compile()


#streamlit ui

st.title("simple graph chat")

user_input = st.text_input("You :")

if st.button("Send"):
   result = app.invoke({
    "message": user_input
   })
   st.success(result["message"])
