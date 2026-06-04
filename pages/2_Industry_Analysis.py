import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏭 Industry Analysis")

df = pd.read_csv("data/startup_data.csv")

industry = df.groupby("Industry").agg({
    "Funding Amount (M USD)":"mean",
    "Valuation (M USD)":"mean",
    "Revenue (M USD)":"mean"
}).reset_index()

fig = px.bar(
    industry,
    x="Industry",
    y="Revenue (M USD)",
    title="Average Revenue by Industry"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(
    df,
    x="Industry",
    y="Valuation (M USD)",
    title="Valuation Distribution by Industry"
)

st.plotly_chart(fig2, use_container_width=True)
