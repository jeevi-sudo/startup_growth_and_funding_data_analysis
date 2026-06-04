import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💎 Valuation Insights")

df = pd.read_csv("data/startup_data.csv")

fig = px.histogram(
    df,
    x="Valuation (M USD)",
    nbins=30,
    title="Valuation Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(
    df,
    y="Valuation (M USD)",
    title="Valuation Spread"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    color="Industry",
    hover_name="Startup Name",
    title="Funding vs Valuation"
)

st.plotly_chart(fig3, use_container_width=True)
