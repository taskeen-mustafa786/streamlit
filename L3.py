import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon="📱", layout="wide")

st.title("🎯 Welcome to My Streamlit App!")

st.write("This simple app lets you interact, explore widgets, and have a little fun along the way!")

# --- User Info ---
st.header("👤 Your Information")

name = st.text_input("What's your name?")
age = st.slider("How old are you?", 10, 80, 20)

st.write(f"👋 Hey **{name or 'there'}!** You’re **{age}** years young.")

# --- Preferences ---
st.header("🎨 Personal Preferences")

col1, col2 = st.columns(2)

with col1:
    color = st.selectbox(
        "Pick your favorite color:",
        ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'Pink', 'Black', 'White', 'Orange']
    )
    st.write(f"🎨 Nice choice — **{color}** looks great!")

with col2:
    happy = st.checkbox("Feeling happy today?")
    if happy:
        st.success("Awesome! Keep shining 😄")
    else:
        st.info("Don’t worry, better moments are on their way 🌈")

# --- Submit ---
if st.button("🎉 Submit"):
    st.balloons()
    st.success(f"Thanks, {name or 'friend'}! You love **{color}**, and you’re **{age}** years young. Keep smiling!")
