import streamlit as st


pg = st.navigation([
    st.Page('pages/home.py',title="Home"),
    st.Page('pages/calculator.py',title= "Calculator"),
    st.Page('pages/make_a_shape.py',title= "Make a Shape"),
    st.Page('pages/community_shapes.py',title= 'Community Shapes'),
    st.Page('pages/quadratic_solver.py',title= 'Quadratic Solver'),
    st.Page('pages/matrix.py',title= "Matrix"),
    st.Page('pages/graph.py',title="Graph"),
    st.Page('pages/random_calcs.py', title="Random Calcs Menu"),
    st.Page('pages/bloxfruits_mastery_calc.py',title="BloxFruits Mastery Calc")
],position="hidden")

pg.run()






#     Insert New row example for later referance
# supabase.table("Shapes").insert({
#     "name": "Python Test",
#     "formula": "x + y",
#     "calculation_type": "Test"
# }).execute()


# 
#    Get col from table
# response = supabase.table("shapes").select("*").eq("id", 5).execute()
# change the .eq("id", 5) to change the id that you get
# 



