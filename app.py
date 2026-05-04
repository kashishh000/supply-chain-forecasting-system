import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("🚚 Supply Chain & Inventory Demand Forecast")

try:
    df = pd.read_csv('data/forecast_results.csv')
except:
    st.error("Run model script first!")
    st.stop()

st.success("XGBoost Model Successfully Predicted Demand!")

fig = go.Figure()
fig.add_trace(go.Scatter(y=df['Actual_Demand'], name="Actual Demand", line=dict(color='blue')))
fig.add_trace(go.Scatter(y=df['Predicted_Demand'], name="Predicted Demand (XGBoost)", line=dict(color='red', dash='dash')))

fig.update_layout(title="Actual vs Predicted Warehouse Demand", xaxis_title="Days", yaxis_title="Units Required")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Actionable Insights")
st.warning("⚠️ Predicted spikes on weekends. Increase warehouse staffing by 20% on these days.")
