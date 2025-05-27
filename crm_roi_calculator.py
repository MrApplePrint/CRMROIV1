
import streamlit as st

def calculate_roi(num_reps, avg_deal_size, conversion_rate, time_saved_per_rep):
    # Calculate increased revenue
    increased_revenue = num_reps * avg_deal_size * conversion_rate
    
    # Calculate time savings
    time_savings = num_reps * time_saved_per_rep * 52  # 52 weeks in a year
    
    # Calculate estimated ROI
    estimated_roi = increased_revenue + time_savings
    
    return increased_revenue, time_savings, estimated_roi

# Streamlit app
st.title("Interactive CRM ROI Calculator")

# Input fields
num_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
avg_deal_size = st.number_input("Average Deal Size (€)", min_value=1, value=10000)
conversion_rate = st.number_input("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=10.0) / 100
time_saved_per_rep = 40 * 0.30  # 30% time savings based on a 40-hour work week

# Calculate ROI
increased_revenue, time_savings, estimated_roi = calculate_roi(num_reps, avg_deal_size, conversion_rate, time_saved_per_rep)

# Display results
st.header("Results")
st.write(f"Increased Revenue: €{increased_revenue:,.2f}")
st.write(f"Time Savings: {time_savings:,.2f} hours/year")
st.write(f"Estimated ROI: €{estimated_roi:,.2f}")
    
