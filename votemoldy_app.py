import streamlit as st

# Set up the page title and look
st.set_page_config(page_title="Vote for Moldy!", page_icon="🍬", layout="centered")
# Inject custom CSS to make the background seafoam green
st.markdown(
    """
    <style>
    .stApp {
        background-color: #A2E8DD;
    }
    /* This makes text inputs look cleaner on the seafoam background */
    .stTextArea textarea {
        background-color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.title(" Smarties Will Vote For Moldy! ")
st.subheader("The Best Candidate for Sophomore Class President")

# A fun intro about your nickname
st.markdown("""
### Hey Sophomores! 
Yes, my nickname is **Moldy** because of my green hair, but my ideas for our class are fresh! 
We all deserve a good student council, so lets make it happen by voting Mildred Robles for sophomore class president!
""")

# Interactive Candy Counter
st.write("---")
st.write("###  Claim your digital Smarties pack!")
if "candy_count" not in st.session_state:
    st.session_state.candy_count = 0

if st.button("Click to grab a pack of Smarties!"):
    st.session_state.candy_count += 1
    st.success(f"You took a pack! Total Smarties handed out: {st.session_state.candy_count}")

# Your Campaign Promises
st.write("---")
st.write("### 📋 My Promises to You:")
st.checkbox("Be a strong voice for sophomores to the administration.")
st.checkbox("Plan events to make our shared lunch building more fun.")
st.checkbox("Keep things transparent and listen to your ideas.")
st.checkbox("Bring unity to our school")

# Footer
st.write("---")
st.caption("Paid for by the Smarties for Moldy Committee. Vote this week!")
st.write("---")
st.write("### 📥 Anonymous Lunchroom Suggestion Box")
st.write("What can I help you with? Let me know anonymously!")

# Text input area for the classmate to type their idea
suggestion = st.text_area("Type your suggestion here:", placeholder="Falcon Friday ideas? Dance activities? Type it here...")

# Submit button logic
if st.button("Submit Suggestion Anonymously"):
    if suggestion.strip() != "":
        # This saves the suggestion to a file named 'suggestions.txt' inside your repository!
        with open("suggestions.txt", "a") as f:
            f.write(suggestion + "\n\n")
        st.success(" Suggestion submitted! Thanks for being a Smartie and helping out.")
    else:
        st.error(" Please type something before hitting submit!")
