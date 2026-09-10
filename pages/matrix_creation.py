import streamlit as st
import numpy as np
st.title("Matrix Creation")
if st.button("<--"):
    st.switch_page("pages/matrix.py")
data = []

st.markdown(f"### {st.session_state['matrix name']}")
cols = st.columns(st.session_state['matrix dimentions'][1])
default_types = [
    'Zero Matrix',
    'Identity Matrix'
    
]
type_of_matrix = st.selectbox(
    "What type of matrix do you want?",
    [default_type for default_type in default_types]
)
for col_num,col in enumerate(cols):
    with col:
        col_values = []
        for i in range(st.session_state['matrix dimentions'][0]):
            value = st.number_input("A", label_visibility="hidden",key= f'col{col}row{i}')
            col_values.append(value)
        data.append(col_values)
data = np.array(data)
print(data)