import streamlit as st
from streamlit.components.v1 import html

# --- PAGE CONFIG --- (must be first Streamlit call)
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"  # Try to open sidebar by default
)

# --- FORCE SIDEBAR VISIBLE (CSS + JS Trick) ---
# CSS to make sidebar visible
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        visibility: visible !important;
        transform: none !important;
        width: 260px !important;
        margin-left: 0 !important;
    }
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# JS to auto-click the sidebar toggle on mobile if collapsed
html("""
<script>
function openSidebar() {
  const selectors = [
    '[data-testid="stSidebarCollapsedControl"]',
    'button[title="Toggle sidebar"]',
    'button[aria-label="Open sidebar"]'
  ];
  for (const sel of selectors) {
    const el = document.querySelector(sel);
    if (el) { el.click(); return true; }
  }
  return false;
}

let attempts = 0;
function tryOpen() {
  attempts += 1;
  if (!openSidebar() && attempts < 8) {
    setTimeout(tryOpen, 400);
  }
}
window.addEventListener('load', tryOpen);
setTimeout(tryOpen, 600);
</script>
""", height=0)

# --- MAIN APP CONTENT ---

st.title("Lesson 02: Layouts and Widgets 🧩")

# --- Sidebar ---
st.sidebar.header("🧍 User Controls")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.slider("Select your age:", 10, 80, 20)

# --- Main Content ---
st.write(f"👋 Hello **{name or 'Guest'}**, You are {age} years old.")

# --- Columns Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎨 Your Preferences")
    color = st.selectbox(
        "Choose a favorite color",
        ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'Pink', 'Black', 'White', 'Orange']
    )
    st.write(f"Your favorite color is **{color}**")

with col2:
    st.subheader("☕ Mood Check")
    happy = st.checkbox("I am feeling happy today!")
    if happy:
        st.success("Keep Smiling 😊")
    else:
        st.warning("Hope your day gets better soon 🌤️")

# --- Button Example ---
if st.button("Submit"):
    st.balloons()
    st.write(f"🎉 Thanks, **{name or 'friend'}**! You selected **{color}** color and you are **{age}** years old.")
