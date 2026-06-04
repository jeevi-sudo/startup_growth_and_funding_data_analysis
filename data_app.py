import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ----------------------------
# Custom Styling
# ----------------------------

st.markdown("""
<style>

.main {
    padding: 1rem;
}

[data-testid="stMetric"] {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load Data
# ----------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/startup_data.csv")

df = load_data()

# ----------------------------
# Sidebar Filters
# ----------------------------

st.sidebar.title("Filters")

industry = st.sidebar.multiselect(
    "Industry",
    options=df["Industry"].unique(),
    default=df["Industry"].unique()
)

region = st.sidebar.multiselect(
    "Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[
    (df["Industry"].isin(industry))
    &
    (df["Region"].isin(region))
]

# ----------------------------
# Title
# ----------------------------

st.title("🚀 Startup Analytics Dashboard")
st.markdown("### Executive Overview")

# ----------------------------
# KPI Cards
# ----------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Total Startups",
        filtered_df.shape[0]
    )

with col2:
    st.metric(
        "Total Funding",
        f"${filtered_df['Funding Amount (M USD)'].sum():,.0f} M"
    )

with col3:
    st.metric(
        "Total Revenue",
        f"${filtered_df['Revenue (M USD)'].sum():,.0f} M"
    )

with col4:
    st.metric(
        "Avg Valuation",
        f"${filtered_df['Valuation (M USD)'].mean():,.0f} M"
    )

# ----------------------------
# Funding by Industry
# ----------------------------

funding = (
    filtered_df.groupby("Industry")
    ["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig = px.bar(
    funding,
    x="Industry",
    y="Funding Amount (M USD)",
    title="Funding by Industry"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Funding vs Valuation
# ----------------------------

fig2 = px.scatter(
    filtered_df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    size="Revenue (M USD)",
    color="Industry",
    hover_name="Startup Name",
    title="Funding vs Valuation"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Insights
# ----------------------------

st.subheader("Business Insights")

top_industry = funding.sort_values(
    "Funding Amount (M USD)",
    ascending=False
).iloc[0]["Industry"]

st.success(
f"""
Highest funded industry: {top_industry}

Average Revenue: ${filtered_df['Revenue (M USD)'].mean():.2f} M

Average Market Share: {filtered_df['Market Share (%)'].mean():.2f} %

Profitability Rate: {round(filtered_df['Profitable'].mean()*100,2)} %
"""
)
