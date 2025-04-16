import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="wide")

# --- NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "About", "Projects", "Contact"],
        icons=["house", "person", "briefcase", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# --- HOME ---
if selected == "Home":
    st.title("👋 Welcome to My Portfolio")
    st.subheader("Hi, I'm Ummey Habiba — a passionate developer and innovator.")
    st.write(
        """
        This website showcases my journey, projects, and how you can get in touch with me.
        Made with ❤️ using Streamlit.
        """
    )

# --- ABOUT ---
elif selected == "About":
    st.title("🙋‍♂️ About Me")
    st.image("https://via.placeholder.com/150", width=150, caption="Your Photo")
    st.write(
        """
        I'm a software developer with expertise in Python, web apps, and machine learning.
        
        - 🛠 Tech Stack: Python, Streamlit, Flask, SQL
        - 🎯 Goals: Build tools that make life easier
        - 🌍 Based in: Anywhere on Earth
        """
    )

# --- PROJECTS ---
elif selected == "Projects":
    st.title("🚀 Projects")
    st.write("Here are a few projects I've worked on:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Data Dashboard")
        st.image("https://via.placeholder.com/300x200", use_column_width=True)
        st.write("An interactive dashboard built using Streamlit and Plotly.")

    with col2:
        st.markdown("### 🤖 Chatbot Assistant")
        st.image("https://via.placeholder.com/300x200", use_column_width=True)
        st.write("An AI-powered chatbot built with Python and OpenAI.")

# --- CONTACT ---
elif selected == "Contact":
    st.title("📬 Contact Me")

    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")

        submitted = st.form_submit_button("Send")

        if submitted:
            st.success("Thanks! Your message has been sent.")

