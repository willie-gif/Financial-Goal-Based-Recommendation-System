import streamlit as st

st.title("Goal-Based Redirector")

# Initialize the session state variable if it doesn't exist
if "Amount" not in st.session_state:
    st.session_state.Amount = None

Saving_amount= st.number_input("Saving Amount: ",min_value=0,value=None)
Saving_Duration= st.number_input("Saving_Duration (Months): ",min_value=0,value=None)

# When the button is clicked, save the answer to session_state
if st.button("Calculate"):
    if Saving_amount is not None and Saving_Duration is not None:
        st.session_state.Amount = Saving_amount * Saving_Duration
    else:
        st.error("Please enter both Saving Amount and Duration.")

# Always display the Amount if it exists in session_state
if st.session_state.Amount is not None:
    amount=st.session_state.Amount
    st.success(f"Total Amount: {amount}")

    # Define thresholds and links
    if amount == 0:
        st.warning("Please enter your savings details to see recommendations.")
    
    elif amount < 50000:
        st.info("Goal: Small Investment / Emergency Fund")
        url = "https://www.ndovu.co"
        st.markdown(f'<a href="{url}" target="_self">Start Investing at Ndovu</a>', unsafe_allow_html=True)

    elif 50000 <= amount < 500000:
        st.info("Goal: Vacation & Experiences")
        url = "https://www.bonfireadventures.com"
        st.markdown(f'<a href="{url}" target="_self">Book with Bonfire Adventures</a>', unsafe_allow_html=True)

    else:
        st.info("Goal: Major Asset (Vehicle)")
        url = "https://khushimotors.com"
        st.markdown(f'<a href="{url}" target="_self">Browse Khushi Motors</a>', unsafe_allow_html=True)
    


