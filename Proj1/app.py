from langchain.llms import OpenAI
#from dotenv import load_dotenv
#load_dotenv()

import streamlit as st
import os

llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),temperature=0.5)

def get_openai_response(question):
    response=llm(question)
    return response
st.set_page_config(page_title="Q&A")

st.header("Langchain App")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("The Response is")
    st.write(response)