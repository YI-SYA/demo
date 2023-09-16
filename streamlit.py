import streamlit as st

#create sidebar
menu = ['Profile','Project']
choice = st.sidebar.selectbox("Select a Page", menu)


#My Profile
if choice == 'Profile':
    st.header("Welcome !!!!")
    st.image("https://giphy.com/embed/qgQUggAC3Pfv687qPC" width="480" height="360" frameBorder="0")

#Project
elif choice == 'Project':
    st.header("Project !!!")
