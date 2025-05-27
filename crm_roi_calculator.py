
import streamlit as st

# Function to calculate CRM ROI
def calculate_roi(num_reps, avg_deal_size, conversion_rate):
    # Constants
    hours_saved_per_rep_per_year = 40 * 10  # 10 weeks per year, 40 hours per week
    
    # Calculations
    increased_revenue = num_reps * avg_deal_size * conversion_rate
    time_savings = num_reps * hours_saved_per_rep_per_year
    estimated_roi = increased_revenue + time_savings
    
    return increased_revenue, time_savings, estimated_roi

# Streamlit app
st.title("Interactive CRM ROI Calculator (Euro)")

# Input fields
num_reps = st.number_input("Number of Sales Reps", min_value=1, value=10)
avg_deal_size = st.number_input("Average Deal Size (€)", min_value=1, value=5000)
conversion_rate = st.number_input("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=20.0) / 100

# Calculate ROI
increased_revenue, time_savings, estimated_roi = calculate_roi(num_reps, avg_deal_size, conversion_rate)

# Display results
st.subheader("Results")
st.write(f"Increased Revenue: €{increased_revenue:,.2f}")
st.write(f"Time Savings: {time_savings:,.0f} hours/year")
st.write(f"Estimated ROI: €{estimated_roi:,.2f}")
