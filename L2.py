import streamlit as st


# Page title
# --- PAGE CONFIG ---
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"  # <--- this line auto-opens sidebar
)

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        visibility: visible;
        width: 260px;
        margin-left: 0;
    }
    [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Lesson 02: Layouts and Widgets 🧩")

# --- Sidebar ---
st.sidebar.header(" User Controls")
name = st.sidebar.text_input(" Enter your name: ")
age = st.sidebar.slider("Select your age: ",10,80,20)

# --- Main Content ---
st.write(f"👋 Hello **{name or 'Guest'}**, You are {age} years old. ")

# --- Columns Layout ---
col1,col2 = st.columns(2)

with col1:
    st.subheader("🎨 Your Preferences")
    color = st.selectbox(f"Choose a favorite color",['Red','Green','Blue','Purple','Yellow','Pink','Black','White','Orange'])
    st.write(f" Your favorite color is {color}")
    
with col2:
    st.subheader("☕ Mood Check")
    happy = st.checkbox(" I am feeling happy, today!")
    
    if happy:
        st.success("Keep Smiling 😊")
    else:
        st.warning("Hope your day gets better soon 🌤️")
        
# --- Button Example ---
if st.button("Submit"):
    st.balloons()
    st.write(f"Thanks, {name or 'friend'}! you selected {color} color and you are {age} years old. ")
    
