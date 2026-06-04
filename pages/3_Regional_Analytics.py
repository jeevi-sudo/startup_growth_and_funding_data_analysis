import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Regional Analytics")

df = pd.read_csv("data/startup_data.csv")

region = (
    df.groupby("Region")
    ["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig = px.pie(
    region,
    names="Region",
    values="Funding Amount (M USD)",
    hole=0.5,
    title="Funding Share by Region"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(
    region,
    x="Region",
    y="Funding Amount (M USD)",
    title="Region Wise Funding"
)

st.plotly_chart(fig2, use_container_width=True)
