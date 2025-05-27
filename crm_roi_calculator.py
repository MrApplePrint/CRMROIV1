
import streamlit as st
import altair as alt
import pandas as pd

def calculate_roi(num_reps, avg_deal_size, num_deals, existing_crm):
    # Constants
    cost_per_rep_per_week = 1000
    weeks_per_year = 52
    
    # Calculate increased revenue
    increased_revenue = num_deals * avg_deal_size
    
    # Calculate time savings
    if existing_crm:
        time_savings_hours = num_reps * 80  # 20% of 400 hours/year
        increased_revenue *= 0.20  # Reduce increased revenue by 80%
    else:
        time_savings_hours = num_reps * 400  # 10 weeks/year
    
    time_savings_value = time_savings_hours * (cost_per_rep_per_week / 40)  # Hourly rate
    
    # Calculate total costs
    total_costs = num_reps * cost_per_rep_per_week * weeks_per_year
    
    # Calculate net ROI
    net_roi = (increased_revenue + time_savings_value) - total_costs
    
    return increased_revenue, time_savings_value, total_costs, net_roi

# Streamlit app
st.title("CRM ROI Calculator")
st.write("""
## Why ServiceNow CRM Should Be Your Only Goal
ServiceNow CRM offers unparalleled integration, automation, and scalability. By choosing ServiceNow, you can:
- **Enhance productivity** with seamless workflows
- **Improve customer satisfaction** through better data insights
- **Achieve higher ROI** with advanced analytics and AI capabilities
""")

# User inputs
num_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
avg_deal_size = st.number_input("Average Deal Size (€)", min_value=1, value=50000)
num_deals = st.number_input("Number of Deals", min_value=1, value=100)
existing_crm = st.checkbox("Do you have an existing CRM?")

# Calculate ROI
increased_revenue, time_savings_value, total_costs, net_roi = calculate_roi(num_reps, avg_deal_size, num_deals, existing_crm)

# Display results
st.write(f"### Increased Revenue: €{increased_revenue:,.2f}")
st.write(f"### Time Savings Value: €{time_savings_value:,.2f}")
st.write(f"### Total Costs: €{total_costs:,.2f}")
st.write(f"### Net ROI: €{net_roi:,.2f}")

# Create a bar chart
data = {
    'Category': ['Increased Revenue', 'Time Savings Value', 'Total Costs', 'Net ROI'],
    'Value': [increased_revenue, time_savings_value, total_costs, net_roi]
}
chart_data = alt.Chart(pd.DataFrame(data)).mark_bar().encode(
    x='Category',
    y='Value'
)

st.altair_chart(chart_data, use_container_width=True)
