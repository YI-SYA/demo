import streamlit as st

#create sidebar
menu = ['Profile','Project']
choice = st.sidebar.selectbox("Select a Page", menu)


#My Profile
if choice == 'Profile':
    st.header("Welcome !!!!")


#Project
elif choice == 'Project':
    st.header("Project !!!")
