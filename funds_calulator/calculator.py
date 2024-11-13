import streamlit as st

# Define color variables to match Business Locus branding
primary_color = "#1a73e8"  # Adjust this color to match the brand's primary color
secondary_color = "#333333"  # Use a dark color for text and headers
highlight_color = "#ffcc00"  # Use a highlight color for results

# Define parameters for the investment plans
pip_min_investment = 25000
pip_roi_15_days = (1.2, 1.5)
pip_roi_30_days = (1.5, 1.8)
pip_risk_ratio = 0.003

oif_min_investment = 200000
oif_roi_30_days = (1.7, 2.5)
oif_roi_45_days = (2.2, 2.5)
oif_risk_ratio = (0.003, 0.005)

# Set up page configuration
st.set_page_config(page_title="Business Locus Investment Calculator")

# Define the app's layout and user interface
st.title("Investment Calculator")
st.subheader("Calculate your potential earnings and risk for Business Locus investment plans")

# Select investment plan
plan = st.selectbox("Select Investment Plan:", ("Physical Inventory Purchasing Fund (PIP Fund)", "Operational Investment Fund (OIF Fund)"))

# Minimum investment based on the selected plan
if plan == "Physical Inventory Purchasing Fund (PIP Fund)":
    st.write(f"Minimum Investment: {pip_min_investment} PKR")
    investment = pip_min_investment
    
    # Select duration and profit percentage for PIP Fund
    duration = st.selectbox("Select Duration:", ("15 Days", "30 Days"))
    if duration == "15 Days":
        profit_percentage = st.slider("Select Profit Percentage:", min_value=pip_roi_15_days[0], max_value=pip_roi_15_days[1], step=0.1)
    else:
        profit_percentage = st.slider("Select Profit Percentage:", min_value=pip_roi_30_days[0], max_value=pip_roi_30_days[1], step=0.1)
    
    # Calculate expected profit and risk
    profit = investment * (profit_percentage / 100)
    risk = investment * pip_risk_ratio

elif plan == "Operational Investment Fund (OIF Fund)":
    st.write(f"Minimum Investment: {oif_min_investment} PKR")
    investment = oif_min_investment
    
    # Select duration and profit percentage for OIF Fund
    duration = st.selectbox("Select Duration:", ("30 Days", "45 Days"))
    if duration == "30 Days":
        profit_percentage = st.slider("Select Profit Percentage:", min_value=oif_roi_30_days[0], max_value=oif_roi_30_days[1], step=0.1)
        risk_ratio = oif_risk_ratio[0]
    else:
        profit_percentage = st.slider("Select Profit Percentage:", min_value=oif_roi_45_days[0], max_value=oif_roi_45_days[1], step=0.1)
        risk_ratio = oif_risk_ratio[1]
    
    # Calculate expected profit and risk
    profit = investment * (profit_percentage / 100)
    risk = investment * risk_ratio

# Display prominent results section with colors matching branding
st.markdown(f"""
    <div style="background-color: {highlight_color}; padding: 20px; border-radius: 10px;">
        <h3 style="color: {secondary_color};">Results</h3>
        <p style="color: {primary_color}; font-size: 18px;">Selected Profit Percentage: {profit_percentage}%</p>
        <p style="color: {primary_color}; font-size: 18px;">Expected Profit: {profit:.2f} PKR</p>
        <p style="color: {primary_color}; font-size: 18px;">Risk: {risk:.2f} PKR</p>
    </div>
""", unsafe_allow_html=True)

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
