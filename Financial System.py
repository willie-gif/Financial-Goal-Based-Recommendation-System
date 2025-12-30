import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Goal Planner", page_icon="💰")
st.title("🎯 Reverse Goal Planner")
st.write("Determine how much you need to save monthly to reach your target asset.")

# --- 1. Data Setup ---
# Mapping goals to their estimated prices and website URLs
goal_data = {
    "Investing (Ndovu)": {
        "price": 5000, 
        "url": "https://www.ndovu.co"
    },
    "Vacation (Bonfire Adventures)": {
        "price": 150000, 
        "url": "https://www.bonfireadventures.com"
    },
    "Vehicle (Khushi Motors)": {
        "price": 1200000, 
        "url": "https://khushimotors.com"
    }
}

# --- 2. User Input Section ---
selected_goal = st.selectbox("What is your ultimate goal?", list(goal_data.keys()))

# Default the price based on selection, but allow the user to edit it
default_price = goal_data[selected_goal]["price"]
target_price = st.number_input("Target Price (KES):", min_value=0, value=default_price)

# Timeframe selection
months = st.slider("In how many months do you want to achieve this?", 1, 60, 12)

# --- 3. Calculation & Display ---
if st.button("Calculate Monthly Requirement"):
    if target_price > 0:
        monthly_needed = target_price / months
        
        # Display the result prominently
        st.divider()
        st.metric(label="Monthly Savings Required", value=f"KES {monthly_needed:,.2f}")
        
        # Advice Logic
        if monthly_needed > (target_price * 0.3):
            st.warning("⚠️ This requires a high monthly commitment. Consider a longer duration.")
        else:
            st.success(f"✅ To reach KES {target_price:,.2f} in {months} months, you need to save KES {monthly_needed:,.2f} per month.")

        # --- 4. The Stylized Redirection Button ---
        target_url = goal_data[selected_goal]["url"]
        
        st.write("---")
        st.info(f"Ready to start? Visit the **{selected_goal}** website to open an account or view listings.")
        
        # Centered HTML Button
        st.markdown(
            f"""
            <div style="text-align: center; padding-top: 10px;">
                <a href="{target_url}" target="_self" style="
                    text-decoration: none; 
                    background-color: #ff4b4b; 
                    color: white; 
                    padding: 12px 24px; 
                    border-radius: 8px; 
                    font-weight: bold;
                    font-size: 18px;
                    display: inline-block;
                    box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                    Go to {selected_goal}
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.error("Please enter a target price greater than 0.")

# --- Sidebar Info ---
st.sidebar.header("About")
st.sidebar.info("This tool helps you plan your financial future by connecting your savings goals with local Kenyan partners.")