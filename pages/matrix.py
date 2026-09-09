import streamlit as st
from pages.matrix_class import Matrix, parse_shape


st.header("Matrix")
if st.button("Home", key="Home button matrix"):
    st.switch_page('pages/home.py')

matrix_name = st.text_input("What is the name of your matrix?")
dimentions_input = st.text_input("Input the dimentions of your matrix. (Row x Col)")

dimentions_of_matrix = parse_shape(dimentions_input)

if dimentions_of_matrix:
    dimentions_of_matrix
else:
    "You neglected a value"


