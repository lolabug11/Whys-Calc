import streamlit as st
from pages.matrix_class import Matrix, parse_shape
if 'matrix name' not in st.session_state:
    st.session_state['matrix name'] = None
if 'matrix dimentions' not in st.session_state:
    st.session_state['matrix name'] = None

st.header("Matrix")
if st.button("Home", key="Home button matrix"):
    st.switch_page('pages/home.py')

st.session_state['matrix name'] = st.text_input("What is the name of your matrix?")
dimentions_input = st.text_input("Input the dimentions of your matrix. (Row x Col)")

st.session_state['matrix dimentions'] = parse_shape(dimentions_input)


if st.session_state['matrix name'] in ["", " "] or st.session_state['matrix name'] is None:
    "Please enter a name for your matrix"
elif st.session_state['matrix dimentions'] == 1 or st.session_state['matrix dimentions'] is None:
    "Your matrix dimentions are not valid please correct the issue"
elif st.session_state['matrix dimentions'] == 0 :
    "Invalid Character was entered"
elif st.session_state['matrix dimentions'][0] == 0:
    "You cant have a matrix with 0 rows"
elif st.session_state['matrix dimentions'][1] == 0:
    "You cant have a matrix with 0 coloumns"
else:
    if st.button("Create Matrix"):
        st.switch_page("pages/matrix_creation.py")
