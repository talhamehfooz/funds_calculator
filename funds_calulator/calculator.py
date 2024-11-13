import streamlit as st

# Define parameters for the investment plans
pip_min_investment = 25000
pip_roi_15_days = (1.2, 1.5)
pip_roi_30_days = (1.5, 1.8)
pip_risk_ratio = 0.003

oif_min_investment = 200000
oif_roi_30_days = (1.7, 2.5)
oif_roi_45_days = (2.2, 2.5)
oif_risk_ratio = (0.003, 0.005)

# Define the app's layout and user interface
st.title("Investment Calculator")
st.subheader("Calculate your potential earnings and risk for Business Locus investment plans")

# Select investment plan
plan = st.selectbox("Select Investment Plan:", ("Physical Inventory Purchasing Fund (PIP Fund)", "Operational Investment Fund (OIF Fund)"))

# Slider for investment amount based on the selected plan
if plan == "Physical Inventory Purchasing Fund (PIP Fund)":
    st.write(f"Minimum Investment: {pip_min_investment} PKR")
    investment = st.slider("Select your investment amount:", min_value=pip_min_investment, max_value=300000, step=1000)
    
    # Select duration for PIP Fund
    duration = st.selectbox("Select Duration:", ("15 Days", "30 Days"))
    
    # Calculate expected profit and risk
    if duration == "15 Days":
        roi = pip_roi_15_days
    else:
        roi = pip_roi_30_days
    
    min_profit = investment * (roi[0] / 100)
    max_profit = investment * (roi[1] / 100)
    risk = investment * pip_risk_ratio

    # Display results
    st.subheader("Results")
    st.write(f"Expected Profit Range: {min_profit:.2f} PKR to {max_profit:.2f} PKR")
    st.write(f"Risk: {risk:.2f} PKR")

elif plan == "Operational Investment Fund (OIF Fund)":
    st.write(f"Minimum Investment: {oif_min_investment} PKR")
    investment = st.slider("Select your investment amount:", min_value=oif_min_investment, max_value=500000, step=1000)
    
    # Select duration for OIF Fund
    duration = st.selectbox("Select Duration:", ("30 Days", "45 Days"))
    
    # Calculate expected profit and risk
    if duration == "30 Days":
        roi = oif_roi_30_days
        risk_ratio = oif_risk_ratio[0]
    else:
        roi = oif_roi_45_days
        risk_ratio = oif_risk_ratio[1]
    
    min_profit = investment * (roi[0] / 100)
    max_profit = investment * (roi[1] / 100)
    risk = investment * risk_ratio

    # Display results
    st.subheader("Results")
    st.write(f"Expected Profit Range: {min_profit:.2f} PKR to {max_profit:.2f} PKR")
    st.write(f"Risk: {risk:.2f} PKR")

# Horizontal layout for action buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Calculate"):
        st.balloons()
with col2:
    if st.button("Start New Calculation"):
        st.experimental_rerun()
with col3:
    if st.button("Invest Now"):
        st.success("Your investment is being processed! You will receive a confirmation shortly.")
