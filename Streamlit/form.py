import streamlit as st

outsideform, inside = st.columns(2)
outsideform.title("Outside form")
inside.title("Inside form")

outside_name = outsideform.text_input(label='Name',value =' ',key='outside_name')
outside_area = outsideform.text_area(label="text_area",key='outside_area')

outsideform.write(f"Name = {outside_name}")
outsideform.write(f"Area = {outside_area}")

with inside.form(key='my_form'):
    inside_name = st.text_input(label='Name',value =' ',key='inside_name')
    inside_area = st.text_area(label="text_area",key = 'inside_area')
    st.form_submit_button('submit',)
    '\n'*5

inside.write(f"Name = {inside_name}")
inside.write(f"Area = {inside_area}")
