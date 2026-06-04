import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Executive Dashboard")

df = pd.read_csv("data/startup_data.csv")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Startups", len(df))
col2.metric("Funding ($M)", round(df["Funding Amount (M USD)"].sum(),2))
col3.metric("Revenue ($M)", round(df["Revenue (M USD)"].sum(),2))
col4.metric("Employees", int(df["Employees"].sum()))

industry = df.groupby("Industry")["Funding Amount (M USD)"].sum().reset_index()

fig = px.bar(
    industry,
    x="Industry",
    y="Funding Amount (M USD)",
    title="Industry Funding Overview"
)

st.plotly_chart(fig, use_container_width=True)
