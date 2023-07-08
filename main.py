import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Search for Happiness')
option = st.selectbox('Select the data for the x axis ',
                      ('GDP',
                       'Happiness',
                       'Social Support',
                       'Corruption'))

option1 = st.selectbox('Select the data for the Y axis ',
                       ('GDP',
                        'Happiness',
                        'Social Support',
                        'Corruption'))
st.subheader(f'{option} and {option1}')


df = pd.read_csv('happy.csv')


figure = px.scatter(x=df[option.lower().replace(' ', '_')], y=df[option1.lower()], labels={'x': option, 'y': option1})
st.plotly_chart(figure)
