import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
#import streamlit_scrollable_textbox as stx
#from distutils.command.build import build

load_dotenv()
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#OpenAI.api_key=os.getenv("OPENAI_API_KEY")

st.sidebar.text('''Hi users this is a simple web application built with Streamlit and powered by OpenAI’s GPT-4. It allows users to automatically generate a personalized self-introduction script by entering basic personal details such as name, age, city, profession, and hobby.
Using the entered data, the app constructs a prompt and sends it to OpenAI’s language model to generate a fluent, natural-sounding introduction. This tool is especially useful for beginners practicing self-introductions, job seekers, or students preparing for interviews or presentation''')

url=os.getenv("profile")
st.sidebar.markdown("check out the source code [link](%s)" % url)

st.title("PYTHON SELF INTRO SCRIPT GENERATOR")

with st.form("Data"):
    name=st.text_input("Name:").strip()
    age=int(st.number_input("Age:"))
    city=st.text_input("City:").strip()
    profession=st.text_input("Profession:")
    hobby=st.text_input("Hobby:")
    button=st.form_submit_button("Generate")

prompt="hey chat-gpt write an intro for me ,my name is "+ name +", my age is " + str(age) + ",my city is "+city+",my profession is"+profession+"and my hobby is "+hobby

if button:
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{"role": "user", "content":prompt }]
    )
    reply=response.choices[0].message.content
    st.code(reply)
    st.success(reply)
else:
    pass
    
