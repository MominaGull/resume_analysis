# Function to suggest improvements based on resume and job description
# This function will analyze the resume and job description and suggest specific improvements
# to enhance the candidate's chances of getting hired.
# It will provide actionable feedback on how to tailor the resume to better match the job description.
# The function takes two parameters: resume (the text of the resume) and job_desc (the text of the job description).
# It constructs a prompt that includes both the resume and job description, asking the model to suggest improvements.
# The response from the model will be a list of specific improvements that the candidate can make.


def suggest_improvements(client, resume, job_desc):
    prompt = f"""
    Based on the following resume and job description, suggest specific improvements the candidate can make to improve their chances of getting hired:
    
    Resume:
    {resume}
    
    Job Description:
    {job_desc}
    Provide a list of actionable feedback on how to tailor the resume to better match the job description.
    Example format:
    1. Improvement 1
    2. Improvement 2
    3. Improvement 3
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a career advisor suggesting improvements to candidates based on their resumes."},
            {"role": "user", "content": prompt}
        ]
    )
    print(response)
    return response.choices[0].message.content
