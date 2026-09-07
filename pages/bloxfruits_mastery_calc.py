import streamlit as st
import json
from math import ceil
from random import randint
st.title("BloxFruits Mastery Calc")
if st.button("Random Cals"):
    st.switch_page("pages/random_calcs.py")
with open("data/mastery_data.json", "r") as file:
    data = json.load(file)
st.markdown('#### Which Mobs are you grinding?')
mobs = []
selected_mobs = {}
for mob in data:
    special_key = f'{mob}'
    selected_mobs[mob] = st.checkbox(mob,key=special_key)
st.markdown('#### Do you want to use an average amount of mastery xp?')
use_average = st.toggle('a',label_visibility="hidden")
st.markdown('#### Do you have 2x Mastery?')
double_mastery = st.toggle('a',label_visibility="hidden",key='2x')
st.markdown("#### What level is your item currently?")
current_lvl = st.number_input('a',label_visibility="hidden",min_value=1,max_value=599)
st.markdown("#### What level do you want your item to be?")
wanted_lvl = st.number_input('a',label_visibility="hidden",min_value=current_lvl+1,max_value=600)
atleast_one_mob_selected = False
mobs_being_grinded = []
mob_group_grinded = []
for mob in selected_mobs:
    if selected_mobs[mob]:
        atleast_one_mob_selected = True
        mobs_being_grinded.append(mob)
        mob_group_grinded.append(0)
        
if atleast_one_mob_selected:
    desired_xp = 0
    current_xp = 0
    for lvl in range(wanted_lvl):
        needed_xp = ceil(lvl**2.26+69)
        desired_xp += needed_xp
    for lvl in range(current_lvl):
        lvl_xp = ceil(lvl**2.26+69)
        current_xp += lvl_xp
    needed_xp = desired_xp - current_xp

    index = 0
    while needed_xp > 0:
        if index > len(mobs_being_grinded)-1:
            index = 0
        current = mobs_being_grinded[index]
        if use_average:
            mob_xp = data[current]["Avg"]
        else:
            mob_xp = randint(data[current]["Min"],data[current]["Max"])
        group_xp = mob_xp * data[current]["in_group"]
        needed_xp -= group_xp
        mob_group_grinded[index] += 1
        index += 1
    'You need to grind, '
    print(mobs_being_grinded)
    for index in range(len(mobs_being_grinded)):
        if not double_mastery:
            f'{mob_group_grinded[index]} groups of {mobs_being_grinded[index]}s'
        else:
            f'{ceil(mob_group_grinded[index]/2)} groups of {mobs_being_grinded[index]}s'

else:
    st.write("Please select a mob.")
