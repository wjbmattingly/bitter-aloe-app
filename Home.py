import streamlit as st
from pathlib import Path
st.sidebar.image(r"./images/bitter_aloe_logo.jpg")
st.markdown("# The Bitter Aloe Project App")

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

home_page = read_markdown_file("markdown_files/home.md")
st.markdown(home_page, unsafe_allow_html=True)
