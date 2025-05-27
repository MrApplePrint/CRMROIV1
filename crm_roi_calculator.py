
import streamlit as st

def calculate_roi(num_sales_reps, avg_deal_size, conversion_rate, time_saved_per_rep):
    # Calculate increased revenue
    increased_revenue = num_sales_reps * avg_deal_size * (conversion_rate / 100)
    
    # Calculate time savings
    time_savings = num_sales_reps * time_saved_per_rep * 52  # Assuming 52 weeks in a year
    
    # Calculate ROI
    roi = increased_revenue + time_savings
    
    return increased_revenue, time_savings, roi

# Streamlit app
st.title("Interactive CRM ROI Calculator")

# Input fields
num_sales_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
avg_deal_size = st.number_input("Average Deal Size (in CAD)", min_value=1, value=5000)
conversion_rate = st.number_input("Conversion Rate (%)", min_value=1, max_value=100, value=20)
time_saved_per_rep = st.number_input("Time Saved per Rep per Week (hours)", min_value=1, value=5)

# Calculate ROI
increased_revenue, time_savings, roi = calculate_roi(num_sales_reps, avg_deal_size, conversion_rate, time_saved_per_rep)

# Display results
st.write(f"Increased Revenue: {increased_revenue} CAD")
st.write(f"Time Savings: {time_savings} hours")
st.write(f"Estimated ROI: {roi} CAD")
