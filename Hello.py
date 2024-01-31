import streamlit as st

# Set the page to wide mode
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Title for your app
st.title('Text Processing App')

st.markdown("""
<style>
    /* Target the buttons inside the Streamlit app to expand to full width */
    .stButton>button {
        width: 100%;
    }
            
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""", unsafe_allow_html=True)

# Creating columns for the layout
col1, col2, col3 = st.columns([3, 1, 3])

# First column for user input text area
with col1:
    user_input = st.text_area("Enter Text Here", height=300)

# Second column for buttons
with col2:
    st.write("")  # This is just to add some space at the top
    summary_btn = st.button("Summary", key="summary_btn")
    classify_btn = st.button("Classify", key="classify_btn")

# Third column for the result text area
with col3:
    result = st.text_area("Result", height=300)

# Functions for summary and classification - Replace with your own functions
def summarize(text):
    # Your summary logic goes here
    return "Summarized text"

def classify(text):
    # Your classification logic goes here
    return "Classification result"

# When the 'Summary' button is pressed
if summary_btn:
    summary_result = summarize(user_input)
    result.text_area("Result", value=summary_result, height=300, key='result')

# When the 'Classify' button is pressed
if classify_btn:
    classification_result = classify(user_input)
    result.text_area("Result", value=classification_result, height=300, key='result')
