from pages.quadratic_solver_functions import *
import streamlit as st
from time import *
import pandas as pd
from math import sqrt
from fractions import Fraction
import numpy as np
st.header("Quadratic Solver")
if st.button("Home", key="Home button quadratic"):
    st.switch_page('pages/home.py')

if "Tabs" not in st.session_state:
    st.session_state["Tabs"] = None

if "Factored_Equation" not in st.session_state:
    st.session_state["Factored_Equation"] = None

if "Standered_Equation" not in st.session_state:
    st.session_state["Standered_Equation"] = None

if "last_tab_with_data_entered" not in st.session_state:
    st.session_state["last_tab_with_data_entered"] = None

if 'a' not in st.session_state:
    st.session_state['a'] = None
if 'b' not in st.session_state:
    st.session_state['b'] = None
if 'c' not in st.session_state:
    st.session_state['c'] = None
standered_form_inputs,factored_form_inputs,outputs,quadratic_function_output = st.tabs(["Standered Form Inputs", "Factored Form Inputs", "Outputs", "Quadratic Function Output"], key="Tabs", on_change="rerun")

with standered_form_inputs:
    a = st.number_input("A",help="Enter The A term of your quadratic", value=1,on_change=standered_form_inputs_input_on_change,min_value=-2**32-1, max_value=2**32-1)
    b = st.number_input("B",help="Enter The B term of your quadratic", value=-5,on_change=standered_form_inputs_input_on_change,min_value=-2**32-1, max_value=2**32-1)
    c = st.number_input("C",help="Enter The C term of your quadratic", value=6,on_change=standered_form_inputs_input_on_change,min_value=-2**32-1, max_value=2**32-1)
    if st.session_state["last_tab_with_data_entered"] == "standered_form_inputs":
        if b >= 0 and c >= 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x + {c}'
        elif b < 0 and c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x - {-c}'
        elif b < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x + {c}'
        elif c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x - {-c}'
        st.session_state['a'] = a
        st.session_state['b'] = b
        st.session_state['c'] = c
        equation_in_factored_form = factor_standered_form_quadratic(a,b,c)
        if equation_in_factored_form:
            st.session_state["Factored_Equation"] = equation_in_factored_form
        else:
            st.session_state["Factored_Equation"] = "This calculator does not correctly calculate the factored form for this equation"
    



with factored_form_inputs:
    factored_equation = st.text_input("Equation",help="Enter your quadratic in factored form.",value="(1x-3.0)(1.0x-2)",on_change=factored_form_inputs_on_change)
    if st.session_state["last_tab_with_data_entered"] == "factored_form_inputs":
        st.session_state["Factored_Equation"] = factored_equation
        standered_equation,a,b,c = parse_factored_form_quadratic(factored_equation)
        st.session_state['a'] = a
        st.session_state['b'] = b
        st.session_state['c'] = c
        if b >= 0 and c >= 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x + {c}'
        elif b < 0 and c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x - {-c}'
        elif b < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x + {c}'
        elif c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x - {-c}'
        # print(standered_equation)




with outputs:
    
    if  st.session_state["Factored_Equation"] == None:
        st.write("Please enter a equation.")
    else:
        round_to = st.number_input("How many decimal places do you want your roots to be rounded to?",value=2,help="1 = tenths place 2 = hundreths place so on so forth")
        a = st.session_state['a']
        b = st.session_state['b']
        c = st.session_state['c']
        roots,identifyer = solve_standered_form(a,b,c)
        
        if identifyer == 1:
            decimal_root_1 = round(float(roots),round_to)
            decimal_root_2 = "N/A"
            fraction_root1 = Fraction(roots).limit_denominator(1000)
        
            fraction_root2 = 'N/A'
            vertex = decimal_root_1
            solution1 = "N/A"
            solution2 = "N/A"
        elif identifyer == 2:    
            fraction_root1 = roots[0]
            fraction_root2 = roots[1]
            vertex = roots[2]
            solution1 = roots[3]
            solution2 = roots[4]
            decimal_root_1 = round((roots[5]),round_to)
            decimal_root_2 = round((roots[6]),round_to)
        else:
            fraction_root1 = "N/A"
            fraction_root2 = "N/A"
            vertex = "This calculator does not calculate the vertex for parabolas with imaginary roots"
            solution1 = "N/A"
            solution2 = "N/A"
            decimal_root_1 = "N/A"
            decimal_root_2 = "N/A"
        data = {"Standered Form":st.session_state["Standered_Equation"],"Factored Equation": st.session_state["Factored_Equation"],"Decimal Root 1":decimal_root_1,"Decimal Root 2":decimal_root_2, "Fraction Root One": fraction_root1,"Fraction Root Two": fraction_root2, "Vertex": vertex,"Solution One":solution1,"Solution Two":solution2}
        st.table(data)

with quadratic_function_output:
    if st.session_state["Factored_Equation"] == None:
        st.write("Please enter a equation.")
    else:
        x = st.number_input("x",help="Enter the number you want the output for",value=0)
        output = (int(st.session_state['a'])*(x**2))+(int(st.session_state['b'])*(x))+(st.session_state['c'])
        if st.session_state['b'] < 0:
            st.session_state['b'] *= -1
            sign1 = '-'
        else:
            sign1 = '+'
        if st.session_state['c'] < 0:
            st.session_state['c'] *= -1
            sign2 = '-'
        else:
            sign2 = '+'
        st.write(f'The output to your quadratic function f({x}) = {st.session_state["a"]}x^2 {sign1} {st.session_state["b"]}x {sign2} {st.session_state["c"]} is {int(output)}')
