
import streamlit as st
import altair as alt
import pandas as pd

# Function to calculate ROI
def calculate_roi(num_reps, avg_deal_size, num_deals, has_existing_crm):
    # Constants
    cost_per_rep_per_week = 1000
    weeks_per_year = 52
    time_savings_per_rep_per_year = 400 if not has_existing_crm else 80  # 10 weeks or 2 weeks
    
    # Calculations
    increased_revenue = num_deals * avg_deal_size
    time_savings_value = num_reps * time_savings_per_rep_per_year * (cost_per_rep_per_week / 40)  # Assuming 40-hour work week
    total_costs = num_reps * cost_per_rep_per_week * weeks_per_year
    net_roi = increased_revenue + time_savings_value - total_costs
    
    return increased_revenue, time_savings_value, total_costs, net_roi

# Streamlit app
st.title("CRM ROI Calculator")

# Inputs
num_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
avg_deal_size = st.number_input("Average Deal Size (€)", min_value=1000, value=50000)
num_deals = st.number_input("Number of Deals", min_value=1, value=100)
has_existing_crm = st.checkbox("Do you have an existing CRM?", value=False)

# Calculate ROI
increased_revenue, time_savings_value, total_costs, net_roi = calculate_roi(num_reps, avg_deal_size, num_deals, has_existing_crm)

# Display results
st.subheader("ROI Results")
st.write(f"Increased Revenue: €{increased_revenue:,.2f}")
st.write(f"Time Savings Value: €{time_savings_value:,.2f}")
st.write(f"Total Costs: €{total_costs:,.2f}")
st.write(f"Net ROI: €{net_roi:,.2f}")

# Data for chart
data = pd.DataFrame({
    'Category': ['Increased Revenue', 'Time Savings Value', 'Total Costs', 'Net ROI'],
    'Amount': [increased_revenue, time_savings_value, total_costs, net_roi]
})

# Altair chart
chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Amount',
    color='Category'
).properties(
    title='ROI Breakdown'
)

st.altair_chart(chart, use_container_width=True)
