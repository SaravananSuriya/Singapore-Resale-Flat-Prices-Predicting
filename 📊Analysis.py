import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import plotly.express as px


st.set_page_config(
    page_title = "EDA of Singapore Resale Flat Price",
    page_icon = "🇸🇬",
    layout = 'wide'
)

rain(
    emoji = "💫",
    font_size = 40,
    falling_speed = 5,
    animation_length = "infinite"
)

colored_header(
    label = 'You are in Data :red[Analysis] page',
    color_name = 'red-70',
    description = ''
)

# df = pd.read_csv('Singapore_Price_Prediction.csv')
@st.cache_data
def filter_data():
    df = pd.read_csv('Singapore_Price_Prediction.csv')
    return df
df = filter_data()

st.markdown("## :red[*Different columns with sum of highest and lowest resale prices*]")
col,col1 = st.columns([2,2])
with col:
    option = st.selectbox("**Select a column**", (['town','flat_type','street_name','storey_range','flat_model']))
with col1:
    choice = st.selectbox("**Select your choice**", (['Highest Values','Lowest Values']))
if choice == 'Highest Values':
    data = df.groupby([option]).sum().reset_index().sort_values('resale_price',ascending=False).head(10)
    # data = df[Column].head(10)
    # st.dataframe(data)
    bar = px.bar(data, x = option, y = 'resale_price', width = 1100, height = 600, labels = {option : option.title(), 'resale_price' : 'Resale Price'}, color_continuous_scale='oxy', color = 'resale_price')
    st.plotly_chart(bar)

    st.markdown("## :red[*column which has sum of top 10 highest count*]")
    data = df.groupby([option]).count().reset_index().sort_values('resale_price',ascending=False).head(10)
    # st.dataframe(data)
    bar = px.bar(data, x = option, y = 'resale_price', width = 1100, height = 600, labels = {option : option.title(), 'resale_price' : 'Count'}, color_continuous_scale='tempo', color = 'resale_price')
    st.plotly_chart(bar)


else:
    data = df.groupby([option]).sum().reset_index().sort_values('resale_price',ascending=True).head(10)
    # data = df[Column].head(10)
    # st.dataframe(data)
    bar = px.bar(data, y = option, x = 'resale_price', orientation = 'h', labels = {option : option.title(), 'resale_price' : 'Resale Price'},width = 1100, height = 600, color_continuous_scale='icefire', color = 'resale_price')
    st.plotly_chart(bar)

    st.markdown("## :red[*column which has sum of top 10 Lowest count*]")
    data = df.groupby([option]).count().reset_index().sort_values('resale_price',ascending=True).head(10)
    # st.dataframe(data)
    bar = px.bar(data, y = option, x = 'resale_price', width = 1100, height = 600, labels = {option : option.title(), 'resale_price' : 'Count'}, orientation = 'h', color_continuous_scale='algae', color = 'resale_price')
    st.plotly_chart(bar)
# st.markdown("## :red[*Different columns which has top 10 highest and lowest count*]")


st.markdown("## :red[*Different columns which contain top 10 highest and lowest resale prices*]")
col,col1 = st.columns([2,2])
with col:
    option = st.selectbox("**select a Column**", (['town','flat_type','street_name','storey_range','flat_model','block','floor_area_sqm','month']))
with col1:
    choice = st.selectbox("**select your Choice**", (['Top 10 Highest Values','Top 10 Lowest Values']))
if choice == 'Top 10 Highest Values':
    data = df[[option,'resale_price']].sort_values('resale_price',ascending=False).head(10)
    # data = df[Column].head(10)
    # st.dataframe(data)
    pie = px.pie(data, names = option, values = 'resale_price', width = 1000, height = 600, labels = {option : option.title(), 'resale_price' : 'Resale Price'})
    st.plotly_chart(pie)
else:
    data = df[[option,'resale_price']].sort_values('resale_price',ascending=True).head(10)
    # data = df[Column].head(10)
    # st.dataframe(data)
    pie = px.pie(data, names = option, values = 'resale_price', width = 1000, height = 600, labels = {option : option.title(), 'resale_price' : 'Resale Price'})
    st.plotly_chart(pie)


@st.cache_data(experimental_allow_widgets=True)
def function():
    st.markdown("## :red[*Overall values for selected column vs Resale Price*]")
    option1 = st.selectbox("**Select a Column**", (['town','flat_type','street_name','storey_range','flat_model','block','floor_area_sqm','month']),index = None)
    if option1 == None:
        st.warning("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ⚠️ **No Column Selected** ⚠️")
    else:
        hist = px.histogram(df, x = option1, y = 'resale_price',width = 1100,height = 600)
        st.plotly_chart(hist)
function()

