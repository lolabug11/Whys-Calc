import streamlit as st
import json
from math import sqrt
st.header("Calculator")

with open("data/defaultShapes.json","r") as file:
    default_shapes = json.load(file)

if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'calc'
else:
    st.session_state['last_page'] = 'calc'


if st.button("Home",key="Home Button Calc"):
    st.switch_page('pages/home.py')
if "custom_shape_name" not in st.session_state:
    st.session_state["custom_shape_name"] = []
if "custom_shape_properties" not in st.session_state:
    st.session_state["custom_shape_properties"] =[]
if "using_custom" not in st.session_state:
    st.session_state["using_custom"] = False

if st.session_state["using_custom"]:

    for shape in range(len(st.session_state['custom_shape_name'])):

        default_shapes[st.session_state['custom_shape_name'][shape]] = st.session_state['custom_shape_properties'][shape]

shape = st.selectbox(
    "Choose a shape",
    [shape for shape in default_shapes]
)
x = None
y = None
z = None

if default_shapes[shape]["number of inputs"] == 1:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0.0,step= 0.001, max_value= float(2**64-1),min_value = float(-2**64-1), format="%.3f",help= "Enter the input to you equation")
    if  x>= 2**64-1 or x <= -2**64-1:
        st.write("Your number is to large enter a new number")
    else:

        result = round(eval(default_shapes[shape]["formula"],{"x1": x,"sqrt":sqrt}),3)
        st.write(f"The {default_shapes[shape]['formula type']} of your {shape} is {result} units")
elif default_shapes[shape]["number of inputs"] == 2:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0.0,step= 0.001, max_value= float(2**64-1),min_value = float(-2**64-1), format="%.3f",help= "Enter the first input to you equation")
    y = st.number_input(f'{default_shapes[shape]["name for the inputs"][1]}',value= 0.0,step= 0.001, max_value= float(2**64-1),min_value = float(-2**64-1), format="%.3f",help= "Enter the second input to you equation",)
    if x >= 2**64-1 or y>= 2**64-1 or x <= -2**64-1 or y< -2**64-1:
        st.write("One of your inputs is to large enter smaller inputs")
    else:
        result = round(eval(default_shapes[shape]["formula"], {
                       "x1": x, "x2": y, "sqrt": sqrt, "sqrt": sqrt}), 3)
        st.write(f"The {default_shapes[shape]['formula type']} of your {shape} is {result} units")
elif default_shapes[shape]["number of inputs"] == 3:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0.0,step= 0.001, max_value= float(2**64-1),min_value = float(-2**64-1), format="%.3f",help= "Enter the first input to you equation")
    y = st.number_input(f'{default_shapes[shape]["name for the inputs"][1]}',value= 0.0,step= 0.001, max_value= float(2**64-1),min_value = float(-2**64-1), format="%.3f",help= "Enter the second input to you equation")
    z = st.number_input(f'{default_shapes[shape]["name for the inputs"][2]}',value= 0.0,step= 0.001, max_value= float(2**64-1),min_value = float(-2**64-1), format="%.3f",help= "Enter the second input to you equation")
    if x >= 2**64-1 or y>= 2**64-1 or z >= 2^64-1 or x <= -2**64-1 or y<= -2**64-1 or z<=-2**64-1:
        st.write("One of your inputs is to large enter smaller inputs")
    else:
        result = round(eval(default_shapes[shape]["formula"], {
                       "x1": x, "x2": y, "x3": z, "sqrt": sqrt}), 3)
        st.write(f"The {default_shapes[shape]['formula type']} of your {shape} is {result} units")
