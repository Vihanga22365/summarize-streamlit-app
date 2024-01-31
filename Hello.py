import streamlit as st
import time

# Set the page to wide mode
st.set_page_config(page_title="Research Application" ,layout="wide", initial_sidebar_state="collapsed")

# Title for your app
st.title('Research Application')

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


# Functions for summary and classification - Replace with your own functions
def summarize(text):
    # Your summary logic goes here
    return "Summarized text"

def classify(text):
    # Your classification logic goes here
    return "Classification result"

# Third column for the result text area
with col3:

    if summary_btn:
      with st.spinner('Summarizing Text...'):
        summary_result = summarize(user_input)
        st.text_area("Result", value=summary_result, height=300, key='result')

    elif classify_btn:
      with st.spinner('Classifying Text...'):
        classification_result = classify(user_input)
        st.text_area("Result", value=classification_result, height=300, key='result')

    else:
      st.text_area("Result", height=300, key='result')
      