import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LinearRegression

# Page setup
st.set_page_config(page_title="Energy Dashboard", layout="wide")

# Load data
df = pd.read_csv("energy_data.csv")
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Hour'] = df['Timestamp'].dt.hour

# Header
st.title("⚡ Energy Consumption Dashboard")

# View raw data
with st.expander("🔍 View Raw Data"):
    st.dataframe(df)

# Hourly average chart
st.subheader("📊 Hourly Average Energy Consumption")
hourly_avg = df.groupby('Hour')['Consumption'].mean()

fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker="o", ax=ax, color='orange')
ax.set_xlabel("Hour")
ax.set_ylabel("Avg kWh")
ax.grid(True, linestyle='--', linewidth=0.5)
st.pyplot(fig)

# Prediction section
st.subheader("🔮 Predict Future Usage")
hour_range = st.slider("Select hours to predict", 10, 23, (10, 14))
model = LinearRegression()
model.fit(df[['Hour']], df['Consumption'])

future_hours = pd.DataFrame({'Hour': list(range(hour_range[0], hour_range[1]+1))})
future_hours['Predicted_kWh'] = model.predict(future_hours)

st.table(future_hours)

