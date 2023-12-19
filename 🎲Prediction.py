import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title = "Singapore Resale Flat Price Prediction",
    page_icon = "🇸🇬",
    layout = 'wide'
)

rain(
    emoji = "❄️",
    font_size = 40,
    falling_speed = 5,
    animation_length = "infinite"
)

colored_header(
    label = 'Welcome to Data :green[Prediction] page 👋🏼',
    color_name = 'green-70',
    description = 'Resale Price Pridiction'
)

@st.cache_data
def filter_data():
    df = pd.read_csv('Singapore_Price_Prediction.csv')
    return df
df = filter_data()

with st.form(key = 'form',clear_on_submit=False):
    type = st.selectbox(
                "**Select a Flat Type**",
                options = df['flat_type'].unique(),
            )
    storey = st.selectbox(
                "**Select a Storey Range**",
                options = df['storey_range'].unique(),
            )
    sqm = st.number_input(f"**Enter Floor Area in (sqm), minimum value is {df['floor_area_sqm'].min()} and maximum value is {df['floor_area_sqm'].max()}**")
    lease_date = st.selectbox(
                "**Select a Lease Commence Date**",
                options = df['lease_commence_date'].unique(),
            )
    town = st.selectbox(
                "**Select a Town**",
                options = df['town'].unique(),
            )
    button = st.form_submit_button('**Predict**',use_container_width = True)

    if button:
        st.markdown("## :green[*Predicted Resale Price is result*]")
# st.dataframe(df.columns)