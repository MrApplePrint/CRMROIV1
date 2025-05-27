
import streamlit as st
import pandas as pd
import altair as alt

# Function to calculate ROI
def calculate_roi(num_reps, avg_deal_size, num_leads, conversion_rate, existing_crm):
    # Calculate number of deals based on leads and conversion rate
    num_deals = num_leads * (conversion_rate / 100)
    
    # Calculate increased revenue
    if existing_crm:
        increased_revenue = num_deals * avg_deal_size * 1.2
    else:
        increased_revenue = num_deals * avg_deal_size * 1.5
    
    # Calculate time savings
    if existing_crm:
        time_savings_hours = num_reps * 80  # 20% of 400 hours/year
    else:
        time_savings_hours = num_reps * 400  # 10 weeks/year
    
    # Calculate time savings value
    time_savings_value = time_savings_hours * (1000 / 40)  # €1000/week per rep
    
    # Calculate total cost
    total_cost = num_reps * 1000 * 52  # €1000/week per rep
    
    # Calculate net ROI
    net_roi = increased_revenue + time_savings_value - total_cost
    
    return increased_revenue, time_savings_value, total_cost, net_roi

# Streamlit app
st.title("CRM ROI Calculator")

# Introduction section
st.header("Why ServiceNow CRM?")
st.write("""
In today's fast-paced business environment, customer relationship management (CRM) is more critical than ever. ServiceNow CRM offers a comprehensive solution that integrates seamlessly with your existing systems, providing real-time insights and automation that drive efficiency and growth.

### Why Now?
- **Increased Competition**: Stay ahead of competitors by leveraging advanced CRM capabilities.
- **Customer Expectations**: Meet and exceed customer expectations with personalized experiences.
- **Operational Efficiency**: Achieve significant time savings and cost reductions through automation.
- **Scalability**: Scale your CRM operations effortlessly as your business grows.
- **Data-Driven Decisions**: Make informed decisions with real-time analytics and reporting.

Adopting ServiceNow CRM now ensures you are equipped to handle the challenges of tomorrow while maximizing your ROI today.
""")

# User inputs
num_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
avg_deal_size = st.number_input("Average Deal Size (€)", min_value=1, value=50000)
num_leads = st.number_input("Number of Leads", min_value=1, value=100)
conversion_rate = st.number_input("Conversion Rate (%)", min_value=1, max_value=100, value=20)
existing_crm = st.checkbox("Do you have an existing CRM?")

# Calculate ROI
increased_revenue, time_savings_value, total_cost, net_roi = calculate_roi(num_reps, avg_deal_size, num_leads, conversion_rate, existing_crm)

# Display results
st.subheader("Results")
st.write(f"Increased Revenue: €{increased_revenue:,.2f}")
st.write(f"Time Savings Value: €{time_savings_value:,.2f}")
st.write(f"Total Cost: €{total_cost:,.2f}")
st.write(f"Net ROI: €{net_roi:,.2f}")

# Create a DataFrame for chart
data = pd.DataFrame({
    'Metric': ['Increased Revenue', 'Time Savings Value', 'Total Cost', 'Net ROI'],
    'Value': [increased_revenue, time_savings_value, total_cost, net_roi]
})

# Create a bar chart using Altair
chart = alt.Chart(data).mark_bar().encode(
    x='Metric',
    y='Value',
    color='Metric'
).properties(
    title='ROI Components'
)

# Display the chart
st.altair_chart(chart, use_container_width=True)
