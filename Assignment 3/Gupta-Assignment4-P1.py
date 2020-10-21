import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import requests
from io import StringIO

url = requests.get('https://drive.google.com/file/d/1VnECEOTY54qjbQ_PwtPPNOJ1OZPKMFC9/view?usp=sharing')
csv_raw = StringIO(url.text)
df = pd.read_csv(csv_raw,header=None)
# FOLDER  = "C:\\Users\\akhilg\Documents\\CollegeDocuments\\BDMA\\CentralSuperlec\\Coursework\\VA\\Assignment 3\\"


# df = pd.read_csv(FOLDER+"\\data\\gender_format1.csv")
year_wise = df.loc[df['Year'].isin([2000,2009,2017]) ]


chart = alt.Chart(df,title="Percentage of Females(%) in Services").mark_line().encode(
    x = 'Year:O',
    y = alt.Y('Services (% of females)',
            axis=alt.Axis(title='percentage of Females(in %)')),
    color = alt.Color('CountryName:N',scale=alt.Scale(scheme='dark2')),
    strokeDash= 'CountryName',
    shape= 'CountryName',
).properties(width=750)

bar = alt.Chart(year_wise,
        title="Across 1999-2017, the ratio of Females to Males in the Services"
    ).mark_bar().encode(
    y= alt.Y('Ratio_service:Q',  ),
    x="Year:O",
    color=alt.Color('Year:N',scale=alt.Scale(range=['red','blue','green'])),
    column ="CountryName:N",
)

st.altair_chart(chart)
st.altair_chart(bar)
