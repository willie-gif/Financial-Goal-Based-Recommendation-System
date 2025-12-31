import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Goal Planner", page_icon="💰")
st.title("🎯 Reverse Goal Planner")
st.write("Determine how much you need to save monthly to reach your target asset.")

# --- 1. Data Setup ---
goal_data = {
    "Investing (Ndovu)": {"price": 5000, "url": "https://www.ndovu.co"},
    "Vacation (Bonfire Adventures)": {"price": 150000, "url": "https://www.bonfireadventures.com"},
    "Vehicle (Khushi Motors)": {"price": 1200000, "url": "https://khushimotors.com"}
}

# --- 2. User Input Section ---
selected_goal = st.selectbox("What is your ultimate goal?", list(goal_data.keys()))

default_price = goal_data[selected_goal]["price"]
target_price = st.number_input("Target Price (KES):", min_value=0, value=default_price)

# Inflation logic ONLY for Vehicle
inflation_rate = 0.0
if "Vehicle" in selected_goal:
    st.info("💡 Note: Vehicles are subject to price changes over time.")
    inflation_input = st.number_input("Annual Inflation Rate (%)", min_value=0.0, max_value=20.0, value=5.0)
    inflation_rate = inflation_input / 100

# Timeframe
months = st.slider("In how many months do you want to achieve this?", 1, 60, 12)

# Group Contribution Feature
st.write("---")
st.subheader("👥 Group Savings")
num_people = st.number_input("Number of people contributing:", min_value=1, value=1, step=1)

# --- 3. Calculation & Display ---
if st.button("Calculate Monthly Requirement"):
    if target_price > 0:
        years = months / 12
        
        # Calculate totals (applying inflation if applicable)
        future_price = target_price * ((1 + inflation_rate) ** years)
        total_monthly_needed = future_price / months
        
        # Calculate per-person contribution
        per_person_needed = total_monthly_needed / num_people
        
        st.divider()
        
        # Display Results
        if "Vehicle" in selected_goal and inflation_rate > 0:
            st.metric(label="Inflation Adjusted Total", value=f"KES {future_price:,.2f}")
        
        col1, col2 = st.columns(2)
        col1.metric(label="Total Monthly (Group)", value=f"KES {total_monthly_needed:,.2f}")
        
        if num_people > 1:
            col2.metric(label="Per Person Monthly", value=f"KES {per_person_needed:,.2f}", delta_color="normal")
            st.success(f"👥 With a group of {num_people}, each person needs to contribute **KES {per_person_needed:,.2f}** monthly.")
        else:
            st.success(f"✅ You need to save **KES {total_monthly_needed:,.2f}** monthly to reach your goal.")

        # --- 4. Redirection Button ---
        target_url = goal_data[selected_goal]["url"]
        st.write("---")
        st.markdown(
            f"""
            <div style="text-align: center; padding-top: 10px;">
                <a href="{target_url}" target="_blank" style="
                    text-decoration: none; 
                    background-color: #ff4b4b; 
                    color: white; 
                    padding: 12px 24px; 
                    border-radius: 8px; 
                    font-weight: bold;
                    display: inline-block;">
                    Go to {selected_goal}
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.error("Please enter a target price greater than 0.")
st.sidebar.info("This tool helps you plan your financial future by connecting your savings goals with local Kenyan partners.")
