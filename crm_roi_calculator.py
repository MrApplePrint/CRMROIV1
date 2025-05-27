
import streamlit as st
import pandas as pd
import altair as alt

# Function to calculate ROI
def calculate_roi(num_deals, avg_deal_value, num_reps, existing_crm):
    # Constants
    cost_per_rep_per_week = 1000
    weeks_per_year = 52
    
    # Calculate increased revenue
    if existing_crm:
        increased_deals = num_deals * 1.2  # 20% uplift
    else:
        increased_deals = num_deals * 1.5  # 50% uplift
    
    increased_revenue = increased_deals * avg_deal_value
    
    # Calculate time savings
    if existing_crm:
        time_saved_per_rep_per_year = 80  # 20% of 400 hours
    else:
        time_saved_per_rep_per_year = 400  # 10 weeks * 40 hours
    
    time_savings_value = num_reps * time_saved_per_rep_per_year * (cost_per_rep_per_week / 40)
    
    # Calculate total cost
    total_cost = num_reps * cost_per_rep_per_week * weeks_per_year
    
    # Calculate net ROI
    net_roi = increased_revenue + time_savings_value - total_cost
    
    return increased_revenue, time_savings_value, total_cost, net_roi

# Streamlit app
st.title("CRM ROI Calculator")
st.write("""
## Why ServiceNow CRM?
ServiceNow CRM offers unparalleled integration, automation, and AI-driven insights, making it the ideal choice for businesses looking to maximize their CRM efficiency and effectiveness.
""")

# User inputs
num_deals = st.number_input("Current Number of Deals", min_value=1, value=100)
avg_deal_value = st.number_input("Average Deal Value (€)", min_value=1, value=50000)
num_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
existing_crm = st.checkbox("Do you have an existing CRM?")

# Calculate ROI
increased_revenue, time_savings_value, total_cost, net_roi = calculate_roi(num_deals, avg_deal_value, num_reps, existing_crm)

# Display results
st.write(f"### Increased Revenue: €{increased_revenue:,.2f}")
st.write(f"### Time Savings Value: €{time_savings_value:,.2f}")
st.write(f"### Total Cost: €{total_cost:,.2f}")
st.write(f"### Net ROI: €{net_roi:,.2f}")

# Create a dataframe for the chart
data = pd.DataFrame({
    'Metric': ['Increased Revenue', 'Time Savings Value', 'Total Cost', 'Net ROI'],
    'Value': [increased_revenue, time_savings_value, total_cost, net_roi]
})

# Create a bar chart
chart = alt.Chart(data).mark_bar().encode(
    x='Metric',
    y='Value',
    color='Metric'
).properties(
    title='ROI Components'
)

st.altair_chart(chart, use_container_width=True)
