import streamlit as st
import numpy as np
import json
st.title("Matrix Creation")
if st.button("<--"):
    st.switch_page("pages/matrix.py")


st.markdown(f"### {st.session_state['matrix name']}")
cols = st.columns(st.session_state['matrix dimentions'][1])
default_types = [
    'Zero Matrix',
    'Identity Matrix',
    'Custom'
]

type_of_matrix = st.selectbox(
    "What type of matrix do you want?",
    [default_type for default_type in default_types]
)   
if type_of_matrix == 'Zero Matrix':
    zero_matrix = []
    for row in range(st.session_state['matrix dimentions'][0]):
        row = []
        for col in range(st.session_state['matrix dimentions'][1]):
            row.append(0)
        zero_matrix.append(row)
    data = np.array(zero_matrix)
    st.table(data,width='content')
elif type_of_matrix == 'Identity Matrix':
    if st.session_state['matrix dimentions'][0] != st.session_state['matrix dimentions'][1]:
        st.write("You cant make an identity matrix with a non square matrix")
    else:
        identity_matrix = []
        for row in range(st.session_state['matrix dimentions'][0]):
            rows = []   
            for col in range(st.session_state['matrix dimentions'][1]):
                if row == col:
                    rows.append(1)
                else:
                    rows.append(0)
            identity_matrix.append(rows)
        data = np.array(identity_matrix)
        st.table(data,width='content')
elif type_of_matrix == 'Custom':
    data = []
    cols = st.columns(st.session_state['matrix dimentions'][1])
    
    for index, col in enumerate(cols):
        col_data = []
        with col:
            for i in range(st.session_state['matrix dimentions'][0]):
                value = st.number_input("A ", label_visibility='hidden', value=0.00,key=f'{index}{i}')
                col_data.append(value)
        data.append(col_data)
    formated_data = []
    for i in range(st.session_state['matrix dimentions'][0]):
        a = []
        for j in range(st.session_state['matrix dimentions'][1]):
            #st.write(f'({j},{i}) = {data[i][j]}')
            a.append(data[j][i])
        formated_data.append(a)
    data = np.array(formated_data)
    

if st.button("Create Matrix"):
    new_data = data.tolist()
    with open('data/matrixData.json','r') as f:
        data = json.load(f)
    data["Matrixes"][st.session_state['matrix name']] = new_data
    with open('data/matroxData.json','w') as f:
        json.dump(data,f)
    st.switch_page("pages/matrix.py")