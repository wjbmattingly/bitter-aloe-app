import streamlit as st
from pathlib import Path

st.markdown("# The Bitter Aloe Project App")
st.sidebar.markdown("# Home")

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

home_page = read_markdown_file("markdown_files/home.md")
st.markdown(home_page, unsafe_allow_html=True)
