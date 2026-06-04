import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

st.title("🤖 Predictive Analytics")

df = pd.read_csv("data/startup_data.csv")

X = df[
    [
        "Funding Rounds",
        "Funding Amount (M USD)",
        "Revenue (M USD)",
        "Employees",
        "Market Share (%)"
    ]
]

y = df["Valuation (M USD)"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

pred = model.predict(X_test)

score = r2_score(y_test,pred)

st.metric(
    "Model R² Score",
    round(score,3)
)

st.write("Feature Importance")

importance = pd.DataFrame({
    "Feature":X.columns,
    "Importance":model.feature_importances_
})

st.dataframe(
    importance.sort_values(
        "Importance",
        ascending=False
    )
)
