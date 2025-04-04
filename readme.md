# Resume Analyzer

A tool to help job seekers analyze their resumes against specific job descriptions using AI.

## Overview

Resume Analyzer is a Streamlit-based web application that leverages OpenAI's API to provide insights on how well a resume matches a job description. The tool offers three main functions:

- **Resume Analysis:** Evaluates how well your resume matches a job description
- **Improvement Suggestions:** Provides actionable feedback to better tailor your resume
- **Missing Keywords:** Identifies important keywords from the job description that are missing in your resume

## Features

- PDF resume upload and parsing
- Job description text input
- Three analysis options via sidebar selection
- Detailed AI-powered feedback on resume-job match

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/resume_analysis.git
   cd resume_analysis
   ```

2. **Create and activate a virtual environment:**
   ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
    pip install streamlit openai python-dotenv pypdf2
   ```

4. **Set up your .env file with your OpenAI API key:**
   ```bash
    OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the Streamlit application:**

   ```bash
   streamlit run main.py
   ```

2. **Upload your resume** (PDF format)
3. **Paste the job description**
4. **Select an analysis option from the sidebar:**
  - **Analyze Resume:** Get overall match assessment
  - **Improvements:** Receive specific suggestions
  - **Keywords:** Identify missing important terms
5. **Click "Upload"** to generate the analysis
6. **Review the insights** to improve your job application

## Project Structure

- **main.py:** Main application file with Streamlit UI
- **analyze.py:** Contains function for resume analysis
- **improvements.py:** Contains function for suggesting improvements
- **keywords.py:** Contains function for extracting missing keywords

## Requirements

- Python 3.7+
- OpenAI API key
- Streamlit
- PyPDF2
- python-dotenv
