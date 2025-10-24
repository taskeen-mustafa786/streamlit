import streamlit as st

st.title("My first streamlit app")
st.write("Hello! buddy?")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Nice to meet you {name}")