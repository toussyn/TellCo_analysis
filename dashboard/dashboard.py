import pandas as pd
import streamlit as st
import numpy as np
import sys, os
import plotly.express as px

# streamlit and strrrrrr

#@st.cache()
def load_data():
    clean_data_df = pd.read_csv("/Users/macbook/MY_PROJECTS/TellCo_analysis/data/clean_df.csv")
    return clean_data_df

clean_df = load_data()

st.title("User Overview Analysis")

st.header('An overview of our data set')
st.write(clean_df)
st.header("Task 1: Top Handsets")
st.write(clean_df['Handset Type'].value_counts())
fig = px.bar(clean_df['Handset Type'].value_counts().rename_axis(
    'Handset Type').reset_index(name='counts').head(10), x='Handset Type', y='counts')
st.plotly_chart(fig)

top_handset_manufacturers = clean_df['Handset Manufacturer'].value_counts(
).head(3)
top_handset_manufacturers = clean_df[clean_df["Handset Manufacturer"].isin(
    top_handset_manufacturers.index.tolist())]
top_handsets = top_handset_manufacturers['Handset Type'].groupby(
    clean_df['Handset Manufacturer']).apply(lambda x: x.value_counts().head(5))
st.header("Top Handsets by manufactureres")
st.dataframe(top_handsets)

st.header("User with the top number of sessions")
number_of_xdr = clean_df.groupby('MSISDN/Number')['MSISDN/Number'].agg(
    'count').reset_index(name='Bearer Id').sort_values(by='Bearer Id', ascending=False)
number_of_xdr.rename(
    columns={number_of_xdr.columns[1]: 'number of xDR sessions'}, inplace=True)
st.dataframe(number_of_xdr.head(10))
fig = px.bar(number_of_xdr.head(10), x='MSISDN/Number',
            y='number of xDR sessions')
fig.update_layout(xaxis_type='category')
st.plotly_chart(fig)


