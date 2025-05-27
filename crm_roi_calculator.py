
import streamlit as st
import pandas as pd
import altair as alt

# Function to calculate ROI
def calculate_roi(num_reps, avg_deal_size, num_deals, cost_per_rep_per_week):
    increased_revenue = num_deals * avg_deal_size
    time_savings_value = num_reps * 400 * (cost_per_rep_per_week / 40)  # 400 hours saved per rep per year
    total_costs = num_reps * cost_per_rep_per_week * 52  # Annual cost per rep
    net_roi = (increased_revenue + time_savings_value) - total_costs
    return increased_revenue, time_savings_value, total_costs, net_roi

# Streamlit app
st.title("CRM ROI Calculator")

# User inputs
num_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
avg_deal_size = st.number_input("Average Deal Size (€)", min_value=1, value=10000)
num_deals = st.number_input("Number of Deals", min_value=1, value=100)
cost_per_rep_per_week = 1000  # Fixed cost per rep per week

# Calculate ROI
increased_revenue, time_savings_value, total_costs, net_roi = calculate_roi(num_reps, avg_deal_size, num_deals, cost_per_rep_per_week)

# Display results
st.subheader("Results")
st.write(f"Increased Revenue: €{increased_revenue:,.2f}")
st.write(f"Time Savings Value: €{time_savings_value:,.2f}")
st.write(f"Total Costs: €{total_costs:,.2f}")
st.write(f"Net ROI: €{net_roi:,.2f}")

# Data for chart
data = pd.DataFrame({
    'Category': ['Increased Revenue', 'Time Savings Value', 'Total Costs', 'Net ROI'],
    'Value': [increased_revenue, time_savings_value, total_costs, net_roi]
})

# Create bar chart using Altair
chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value',
    color='Category'
).properties(
    title='ROI Components'
)

# Display chart
st.altair_chart(chart, use_container_width=True)
    
