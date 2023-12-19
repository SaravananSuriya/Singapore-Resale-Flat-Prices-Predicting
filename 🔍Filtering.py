import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import streamlit_pandas as sp

st.set_page_config(
    page_title = "Data Filtering",
    page_icon = "📁",
    layout = 'wide'
)

rain(
    emoji = "💧",
    font_size = 40,
    falling_speed = 5,
    animation_length = "infinite"
)

# st.markdown("# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; You are in Data :blue[Filtering] page")
# st.markdown("""---""")
colored_header(
    label = 'You are in Data :blue[Filtering] page',
    color_name = 'blue-70',
    description = ''
)
@st.cache_data
def filter_data():
    df = pd.read_csv('Singapore_Price_Prediction.csv')
    return df
df = filter_data()

filter = dataframe_explorer(df)
button = st.button('**SUBMIT**',use_container_width = True)
if button:
    st.dataframe(filter,use_container_width = True,hide_index=True)
choice = st.sidebar.selectbox(label = '*Select a column to know unique value :*',options = ['block','town','storey_range','street_name','flat_model'],index=None)
if choice == 'block':
    unique_blocks = df['block'].unique()
    unique_blocks_df = pd.DataFrame({'Unique_Block': unique_blocks})
    st.sidebar.dataframe(unique_blocks_df,use_container_width = True)
elif choice == 'town':
    unique_town = df['town'].unique()
    unique_town_df = pd.DataFrame({'Unique_Town': unique_town})
    st.sidebar.dataframe(unique_town_df,use_container_width = True)
elif choice == 'storey_range':
    unique_storey_range = df['storey_range'].unique()
    unique_storey_range_df = pd.DataFrame({'Unique_Storey_Range': unique_storey_range})
    st.sidebar.dataframe(unique_storey_range_df,use_container_width = True)
elif choice == 'street_name':
    unique_street_name = df['street_name'].unique()
    unique_street_name_df = pd.DataFrame({'Unique_Street_Name': unique_street_name})
    st.sidebar.dataframe(unique_street_name_df,use_container_width = True)
elif choice == 'flat_model':
    unique_flat_model = df['flat_model'].unique()
    unique_flat_model_df = pd.DataFrame({'Unique_Flat_Model': unique_flat_model})
    st.sidebar.dataframe(unique_flat_model_df,use_container_width = True)
# @st.cache_data
# def filter_data():
#     df = pd.read_csv('ResaleFlatPricesBasedonApprovalDate2000Feb2012.csv')
#     return df
# df = filter_data()

# option = {
#     "month" : "multiselect",
#     "town" : "multiselect",
#     "flat_type" : "multiselect",
#     "block" : "multiselect",
#     "street_name" : "multiselect",
#     "storey_range" : "multiselect",
#     "flat_model" : "multiselect"
# }

# all_widgets = sp.create_widgets(df, option)
# # result = sp.filter_df(df, all_widgets)
# button = st.button("submit")
# try:
#     if button:
#         result = sp.filter_df(df, all_widgets)
#         st.write(result)
# except:
#     st.warning("NO DATA AVAILABLE FOR SELECTED OPTIONS")

# data = df[(df['month'] == '2000-01')&(df['town'] == 'ANG MO KIO')&(df['flat_type'] == '1 ROOM')&(df['block'] == '1')&(df['street_name'] == 'ADMIRALTY DR')&(df['storey_range'] == '01 TO 03')&(df['floor_area_sqm'] == 153.52)&(df['flat_model'] == '2-room')&(df['lease_commence_date'] == 1998)&(df['resale_price'] == 424178.19)]
# st.write(data)