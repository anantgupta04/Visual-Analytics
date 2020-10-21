import streamlit as st
import pandas as pd
import altair as alt
from altair import datum
import numpy as np

# read file
# FOLDER  = "C:\\Users\\akhilg\Documents\\CollegeDocuments\\BDMA\\CentralSuperlec\\Coursework\\VA\\Assignment 3\\"
# df = pd.read_csv(FOLDER+"\\data\\gender_format1.csv")
url = requests.get('https://drive.google.com/file/d/1VnECEOTY54qjbQ_PwtPPNOJ1OZPKMFC9/view?usp=sharing')
csv_raw = StringIO(url.text)
df = pd.read_csv(csv_raw,header=None)

china = df.loc[df['CountryName'].isin(["China"])]

# st.header("Welcome to a visual full of deceits.")

# chart to falsely lead people to believe that there more females than males in the industry
chart1 = alt.Chart(china,title="Difference between the male% and the female% youth(15-24) working in industry").mark_bar().encode(
	# align="left",
	x="Year:O",
    y=alt.Y("diff_young:Q"),
    color=alt.condition(
        datum.diff_young > 0,
        alt.value("green"),  # The positive color
        alt.value("red")  # The negative color
    ),
	row="CountryName"
).transform_filter(
	(datum.diff_young <= 3)
).properties(width=750)

st.altair_chart(chart1)


# chart to propogate feelings of angst for the females in Brazil and South Africa
chart2 = alt.Chart(df,title="Rate of Female UnEmployment in BRIC countr").mark_line().encode(
    x = 'Year:O',
    y = alt.Y('UnemploymentFemale',
            axis=alt.Axis(title='Female Unemployment')),
    color = alt.Color('CountryName:N',scale=alt.Scale(scheme='dark2')),
    strokeDash= 'CountryName',
    shape= 'CountryName',
).transform_filter(
	(datum.unemployDiff >= 0.5)
).properties(width=750)

# st.altair_chart(bar4)
st.altair_chart(chart2)
