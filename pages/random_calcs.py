import streamlit as st
st.title("Random Calcs")
if st.button("Home"):
    st.switch_page("pages/home.py")
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("BloxFruits Mastery Calc"):
        st.switch_page("pages/bloxfruits_mastery_calc.py")
