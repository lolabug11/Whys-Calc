import streamlit as st
lcol,middle_col,rcol = st.columns([1,2,1])
with middle_col:
    st.title("Home",text_alignment="center")
l_col,mid_col,r_col = st.columns(3)
if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'home'
else:
    st.session_state['last_page'] = 'home'

with l_col:
    left_col,middle_col,right_col = st.columns([1,2,1])
    with middle_col:
        if st.button("Calculator"):
            st.switch_page("pages/calculator.py")
        if st.button("Matrix"):
            st.switch_page("pages/matrix.py")
        
with mid_col:
    left_col,middle_col,right_col = st.columns([1,2,1])
    with middle_col:
        if st.button("Community Shapes"):
            st.switch_page("pages/community_shapes.py")
        if st.button("Quadratic Solver"):
            st.switch_page("pages/quadratic_solver.py")
with r_col:
    left_col,middle_col,right_col = st.columns([1,2,1])
    with middle_col:
        if st.button("Make a Shape"):
            st.switch_page("pages/make_a_shape.py")
        if st.button("Graph"):
            st.switch_page("pages/graph.py")
