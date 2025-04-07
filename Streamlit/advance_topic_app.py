import streamlit as st

main_page =st.Page("main_page_py.py",icon="🔥",title="main Page")
page_2 = st.Page("page_2.py", icon="🎈", title="page_2")
page_3 = st.Page("page_3.py", icon="🎉", title="page_3")

pg = st.navigation([main_page,page_2,page_3])

pg.run()