import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Funding Analytics")

df = pd.read_csv("data/startup_data.csv")

# Funding Distribution

fig = px.histogram(
    df,
    x="Funding Amount (M USD)",
    nbins=30,
    title="Funding Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Top Funded Startups

top = df.nlargest(
    10,
    "Funding Amount (M USD)"
)

fig2 = px.bar(
    top,
    x="Startup Name",
    y="Funding Amount (M USD)",
    title="Top 10 Funded Startups"
)

st.plotly_chart(fig2, use_container_width=True)
