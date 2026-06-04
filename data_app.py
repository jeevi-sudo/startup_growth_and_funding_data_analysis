import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main {
    padding: 1rem;
}

.kpi-card {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/startup_data.csv")

df = load_data()

# -----------------------------
# Banner
# -----------------------------
try:
    st.image("assets/banner.png", use_container_width=True)
except:
    pass

# -----------------------------
# Title
# -----------------------------
st.title("🚀 Startup Analytics Dashboard")
st.markdown(
    """
    Analyze startup funding, valuation, revenue,
    profitability, industry trends, regional performance,
    and predictive insights.
    """
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Dashboard Navigation")
st.sidebar.success(
    """
    Use the pages menu above to explore:

    📊 Executive Dashboard

    💰 Funding Analytics

    💎 Valuation Insights

    🏭 Industry Analysis

    🌍 Regional Analytics

    🤖 Predictive Analytics
    """
)

# -----------------------------
# KPI Metrics
# -----------------------------
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Startups",
        len(df)
    )

with col2:
    st.metric(
        "Total Funding ($M)",
        f"{df['Funding Amount (M USD)'].sum():,.0f}"
    )

with col3:
    st.metric(
        "Total Revenue ($M)",
        f"{df['Revenue (M USD)'].sum():,.0f}"
    )

with col4:
    st.metric(
        "Avg Valuation ($M)",
        f"{df['Valuation (M USD)'].mean():,.0f}"
    )

# -----------------------------
# Funding by Industry
# -----------------------------
st.subheader("Funding by Industry")

industry_funding = (
    df.groupby("Industry")["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    industry_funding,
    x="Industry",
    y="Funding Amount (M USD)",
    title="Total Funding by Industry"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Funding vs Valuation
# -----------------------------
st.subheader("Funding vs Valuation")

fig2 = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    color="Industry",
    size="Revenue (M USD)",
    hover_name="Startup Name",
    title="Funding vs Valuation Analysis"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Top 10 Funded Startups
# -----------------------------
st.subheader("Top 10 Funded Startups")

top10 = df.nlargest(
    10,
    "Funding Amount (M USD)"
)

fig3 = px.bar(
    top10,
    x="Startup Name",
    y="Funding Amount (M USD)",
    title="Top Funded Startups"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Business Insights
# -----------------------------
st.subheader("📈 Automated Business Insights")

top_industry = (
    industry_funding.sort_values(
        "Funding Amount (M USD)",
        ascending=False
    )
    .iloc[0]["Industry"]
)

highest_valuation = (
    df.loc[
        df["Valuation (M USD)"].idxmax(),
        "Startup Name"
    ]
)

avg_market_share = round(
    df["Market Share (%)"].mean(),
    2
)

st.success(f"""
✓ Highest funded industry: {top_industry}

✓ Startup with highest valuation: {highest_valuation}

✓ Average market share: {avg_market_share}%

✓ Total startups analyzed: {len(df)}

✓ Explore detailed insights using the pages in the left sidebar.
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "Built using Python, Pandas, Plotly, Streamlit, and Scikit-Learn"
)
