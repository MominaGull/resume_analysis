# Function to extract missing keywords from resume based on job description
# This function will analyze the resume and job description and identify the top 10 keywords from the job description
# that are missing in the resume.
# It will provide a list of keywords that the candidate should consider adding to their resume.
# The function takes two parameters: resume (the text of the resume) and job_desc (the text of the job description).
# It constructs a prompt that includes both the resume and job description, asking the model to identify missing keywords.
# The response from the model will include a list of keywords that are present in the job description but missing in the resume.


def extract_keywords(client, resume, job_desc):
    prompt = f"""
    Compare the following resume and job description. Identify all the relevant keywords from the job description that are missing in the resume:
    
    Resume:
    {resume}
    
    Job Description:
    {job_desc}
    Provide the reuslts as a list of keywords that are missing in the resume.
    Example format:
    1. Keyword 1
    2. Keyword 2
    3. Keyword 3
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
                "content": "You are an ATS analyzer identifying missing keywords to help candidates evaluate their resumes."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
