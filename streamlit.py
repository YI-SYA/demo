import streamlit as st

#create sidebar
menu = ['Profile','Project']
choice = st.sidebar.selectbox("Select a Page", menu)


#My Profile
if choice == 'Profile':
    st.header("<h1 style='font-size: 36px;'>### 👨‍🔧 Welcome !!!!</h1>", unsafe_allow_html=True")


#Project
elif choice == 'Project':
    st.header("Project !!!")
