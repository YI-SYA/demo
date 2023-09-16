import streamlit as st



# create sidebar
menu = ['Profile', 'Project']
choice = st.sidebar.selectbox("Select a Page", menu)


# My Profile
if choice == 'Profile':#welcome
    with st.container():
        st.title("Helloo, Welcome to My Profile")
        st.header("my name is _Muhyiddin Syarif_ :F39F5A", divider='rainbow')
        st.header("I'm Data Science progammer from Indonesia")
    st.write("---")
    with st.container():
        st.image("https://img.freepik.com/free-vector/hand-drawn-web-developers_23-2148819604.jpg?w=1060&t=st=1694832376~exp=1694832976~hmac=71108d0b0e08c88ca08d8cf38b5b6161cdbe8a0806c7faab045a81880dd61e69")
    st.write("---")
    with st.container():
        st.write("")
    with st.container():
        st.header("List of Project")

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
    st.header("Prediksi Unburn Carbon Batubara PLTU")\

    with st.container():
        st.image("https://img.freepik.com/free-vector/industrial-factory-power-plant-illustration-facility-with-chimneys-producing-smoke-heavy-chemicals-global-warming-air-pollution-problem_575670-468.jpg?w=1060&t=st=1694833359~exp=1694833959~hmac=52b8bac1675c817649c0983bd16d9927994ba0dfa80022222b1de357954719fc")
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
    
