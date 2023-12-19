import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain

st.set_page_config(
    page_title = "Project Description",
    page_icon = "📚",
    layout = 'wide'
)

rain(
    emoji = "🎊",
    font_size = 40,
    falling_speed = 5,
    animation_length = "infinite"
)

# st.markdown('# &nbsp; &nbsp; &nbsp; &nbsp;  Welcome to :green[Home] Page')

column1,column2,column3 = st.columns([1,3,1], gap = 'small')

# with column2:
#     st.markdown('# &nbsp; &nbsp; &nbsp; &nbsp;  Welcome to :green[Home] Page')
# st.markdown("""---""")
# st.title("Project Title :")
colored_header(
    label = 'Welcome to :orange[Home] Page 👋🏼',
    color_name = 'orange-70',
    description = '',
)

with st.form(key = 'form',clear_on_submit=False):

    st.markdown("## :orange[*Project title*:]")
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Singapore  Resale Flat Prices Predicting*")
    st.markdown("## :orange[*Skills take away From This Project*:]")
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Data Wrangling, EDA, Model Building, Model Deployment.*")
    st.markdown("## :orange[*Domain*:]")
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Real Estate*")
    st.markdown("## :orange[*Problem Statement:*]")
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore.*")
    st.markdown("## :orange[*Results:*]")
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *The project will benefit both potential buyers and sellers in the Singapore housing market. Additionally, the project demonstrates the practical application of machine learning in real estate and web development.*")
    # st.markdown("## :orange[*Dataset:*]")
    button = st.form_submit_button('**Click here to get Data Set Link**',use_container_width = True)
    if button:
        url = "https://beta.data.gov.sg/collections/189/view"
        st.markdown("## :orange[Dataset : [Data Link](%s)]"% url)

