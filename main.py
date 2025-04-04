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
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Title and description
st.title("Resume Analyzer")
st.write("Upload your resume and paste the job description to get insights.")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Job description input
job_description = st.text_area("Paste the job description here:")

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
    else:
        # Call OpenAI based on the selected option
        if option == "Analyze Resume":
            response = analyze_resume(client, resume_text, job_description)
        elif option == "Improvements":
            response = suggest_improvements(
                client, resume_text, job_description)
        elif option == "Keywords":
            response = extract_keywords(client, resume_text, job_description)

        st.subheader("Analysis Results:")
        st.write(response)
