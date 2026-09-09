import streamlit as st
from graph_class import *
st.header("Graph")
if st.button("Home", key="Home button graph"):
    st.switch_page('pages/home.py')
st.write("Work in progress")
