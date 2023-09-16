import streamlit as st

#create sidebar
menu = ['Profile','Project']
choice = st.sidebar.selectbox("Select a Page", menu)


#My Profile
if choice == 'Profile':
    st.header("Welcome !!!)


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
