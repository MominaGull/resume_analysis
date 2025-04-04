import os
from dotenv import load_dotenv

from openai import OpenAI

import streamlit as st
from PyPDF2 import PdfReader

from analyze import analyze_resume
from improvements import suggest_improvements
from keywords import extract_keywords

load_dotenv(override=True)
# Load environment variables from .env file
# Set the OpenAI API key
default_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Title and description
st.title("Resume Analyzer")
st.write("Upload your resume and paste the job description to get insights.")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Job description input
job_description = st.text_area("Paste the job description here:")

# Sidebar for API key and options
st.sidebar.title("Settings")

# API key input in sidebar
user_api_key = st.sidebar.text_input("Enter your OpenAI API Key:",
                                     type="password",
                                     help="Your API key will not be stored and is only used for this session")

# Use user provided API key if available, otherwise fall back to environment variable
api_key = user_api_key if user_api_key else default_api_key

# Sidebar options
option = st.sidebar.selectbox(
    "Choose an option:",
    ["Analyze Resume", "Improvements", "Keywords"]
)

# Function to parse PDF


def parse_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    print(text)
    return text


# Store parsed resume text
resume_text = None
if uploaded_file:
    resume_text = parse_pdf(uploaded_file)
    st.success("Resume uploaded and parsed successfully")

# Analyze button
if st.button("Upload"):
    if not resume_text:
        st.error("Please upload a resume.")
    elif not job_description:
        st.error("Please enter a job description.")
    elif not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    else:
        try:
            # Create OpenAI client with the API key
            client = OpenAI(api_key=api_key)
            # Call OpenAI based on the selected option
            if option == "Analyze Resume":
                response = analyze_resume(client, resume_text, job_description)
            elif option == "Improvements":
                response = suggest_improvements(
                    client, resume_text, job_description)
            elif option == "Keywords":
                response = extract_keywords(
                    client, resume_text, job_description)

            st.subheader("Analysis Results:")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {str(e)}")
            if "API key" in str(e).lower():
                st.error("Please check if your OpenAI API key is valid.")
