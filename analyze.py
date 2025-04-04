# Function to analyze resume and job description
# This function will analyze the resume and job description and provide insights into the candidate's strengths and weaknesses.
# It will also give an overall assessment of whether the candidate is a strong fit for the role.
# The function takes two parameters: resume (the text of the resume) and job_desc (the text of the job description).
# It constructs a prompt that includes both the resume and job description, asking the model to analyze them.
# The response from the model will include the candidate's strengths, weaknesses, and an overall assessment.


def analyze_resume(client, resume, job_desc):
    prompt = f"""
    Analyze the given resume and the job description:
    
    Resume:
    {resume}
    
    Job Description:
    {job_desc}
    
    Throrughly compare, match and analyze the resume with the provided job description and provide the following:
    1. Strengths of the candidate for this role.
    2. Weaknesses of the candidate for this role.
    3. Overall assessment: Is the candidate a strong fit for the role? Why or why not?
    Provide these insights in a structured format. Analysis should be added as bullet points.
    Example format:
    1. Strengths:
       - Strength 1
       - Strength 2
    2. Weaknesses:
       - Weakness 1
       - Weakness 2
    3. Overall Assessment:
       - Overall Assessment
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert resume analyzer and help candidates with analyzing their "
             "reusmes for different jobs."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
