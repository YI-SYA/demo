import streamlit as st
st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: monospace;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    color: white;
    font-family: monospace;
}
[class^="st-b"]  {
    color: white;
    font-family: monospace;
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: #0c0080;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #0c0080;
}
header .decoration {
    background-image: none;
}

</style>
""",
    unsafe_allow_html=True,
)

# create sidebar
menu = ['Profile', 'Project']
choice = st.sidebar.selectbox("Select a Page", menu)


# My Profile
if choice == 'Profile':
    st.header("Welcome !!!!")
    st.title("My Name is Muhyiddin Syarif")
    st.image()


# Project
elif choice == 'Project':
    st.header("Project !!!")
    
    #model = pickle.load(open('unburn_carbon.sav', 'rb'))

    st.title('Prediksi Unburn Carbon')


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

    if st.button('Estimasi hasil Unburn Carbon'):
        predict = model.predict(
            [[nilai_kalor, co, co2, out_generator, sfc, eco_gas_out_temp, pa_flow, o2, fuel_temp, sa_flow, carbon,
                hydrogen, nitrogen, sulfur, ash, total_moisture, oxygen, surface_moisture, inherent_moisture]]
        )
        st.write('Besar hasil Unburn Carbon =', predict, '%')
