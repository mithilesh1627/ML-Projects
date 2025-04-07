import streamlit as st
import time

# Display a placeholder first
placeholder = st.empty()
placeholder.text("⏳ Loading data...")
time.sleep(0.9)
placeholder.success("✅ Data loaded successfully!")

st.success("success")
with st.spinner("fhg",show_time=True):
    time.sleep(10)
    st.balloons()
    st.snow()

