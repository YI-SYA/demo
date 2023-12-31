import streamlit as st
import pickle



# create sidebar
menu = ['Profile', 'Project']
choice = st.sidebar.selectbox("Select a Page", menu)


# My Profile
if choice == 'Profile':#welcome
    with st.container():
        st.title("Helloo, Welcome to My Profile")
        st.header("my name is  :red[_Muhyiddin Syarif_]", )
        st.write("I'm Data Science progammer from Indonesia")
    st.write("---")
    with st.container():
        st.image("https://img.freepik.com/free-vector/hand-drawn-web-developers_23-2148819604.jpg?w=1060&t=st=1694832376~exp=1694832976~hmac=71108d0b0e08c88ca08d8cf38b5b6161cdbe8a0806c7faab045a81880dd61e69", use_column_width=None)
    st.write("---")
    with st.container():
        st.write("")
    with st.container():
        tab, gambar = st.columns(2)
        with tab:
            tab1, tab2 = st.tabs(["List of Project", "My Profile"])
            with tab1:
                st.header(':red[List of Project]')
                st.subheader('- Prediksi listrik yang dihasilkan PLTU')
                st.subheader('- Prediksi Nilai Unburn Carbon Batubara PLTU')
                st.subheader(' ')
                st.caption(':red[*klik pada side bar untuk melihat project]')
            with tab2:
                st.header(':red[My Profile]')
                st.text('- Name   : Muhyiddin Syarif')
                st.text('- Sex    : Male')
                st.text('- Birth  : April 09, 2001')
                st.text('- Nation : Indonesia')
                st.text('- Status : Single')
        with gambar:
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.image("https://img.freepik.com/free-vector/hand-drawn-web-developers_23-2148819604.jpg?w=1060&t=st=1694832376~exp=1694832976~hmac=71108d0b0e08c88ca08d8cf38b5b6161cdbe8a0806c7faab045a81880dd61e69", use_column_width="auto")

        
        
        
        

    #contact container
    with st.container():
        st.write("---")
        st.header("Contact Me")
        email,whatsapp,instragram,facebook = st.columns(4)
        with email:
            st.write("my email")
            st.write("test@gmail.com")
        with whatsapp:
            st.write("my whatsapp")
            st.write("test")
        with instragram:
            st.write("my Instagram")
            st.markdown("[My instagram](https:www.instagram.com)")
        with facebook:
            st.write('my facebook')
            st.markdown("[my facebook](https:www.facebook.com)")
        


# Project
elif choice == 'Project':
    st.header("Prediksi Unburn Carbon Batubara PLTU")
    st.write("---")
    st.caption(':red[*Mean Absolute Error (MAE): 0.27]')
    model = pickle.load(open('unburn_model2.pkl', 'rb'))


    with st.container():
        var1, var2 = st.columns(2)
        with var1:
            nilai_kalor = st.number_input('Input nilai kalor (kcal/kg) ')
            co = st.number_input('Input Co (%) ')
            co2 = st.number_input('Input CO2 (%) ')
            out_generator = st.number_input('Input Output generator (MW) ')
            sfc = st.number_input('Input SFC (kg/kWh) ')
            eco_gas_out_temp = st.number_input('Eco gas Outlet Temperatur (C) ')
            pa_flow = st.number_input('Input PA Flow (T/H) ')
            o2 = st.number_input('Input O2 Outlet APH  (%) ')
            fuel_temp = st.number_input('Input fuel temperature (C) ')
            sa_flow = st.number_input('Secondary Air (T/H) ')
        with var2:
            carbon = st.number_input('Input carbon (%) ')
            hydrogen = st.number_input('Input Hydrogen (%) ')
            nitrogen = st.number_input('Input nitrogen (%) ')
            sulfur = st.number_input('Input Sulfur (%) ')
            ash = st.number_input('Input ash (%) ')
            total_moisture = st.number_input('Input total_moisture ( %) ')
            oxygen = st.number_input('Input SFC (%) ')
            surface_moisture = st.number_input('input surface_moisturer (%) ')
            inherent_moisture = st.number_input('Input inherent_moisture (%) ')
            predict = ''
    st.write("---")
    with st.container():
        if st.button('Estimasi hasil Unburn Carbon'):
            predict = model.predict(
                [[nilai_kalor, co, co2, out_generator, sfc, eco_gas_out_temp, pa_flow, o2, fuel_temp, sa_flow, carbon,
                    hydrogen, nitrogen, sulfur, ash, total_moisture, oxygen, surface_moisture, inherent_moisture]]
            )
            st.write('Besar hasil Unburn Carbon =', predict, '%')
    
