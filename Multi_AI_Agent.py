from dotenv import load_dotenv
load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="Resume Analyzer")
st.header("Resume Analyzer")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Add options for Student POV and Recruiter POV
option = st.radio("Choose Perspective:", ("Student POV", "Recruiter POV"))

# Define prompts for each perspective
student_prompt1 = """
You are a career counselor helping a student improve their resume. Analyze the resume and provide feedback on how the student can better align their skills, experiences, and education with the job description. 
Focus on areas for improvement, such as missing skills, weak phrasing, or lack of relevant experience. Provide actionable advice for the student to enhance their resume.
"""

student_prompt2 = """
You are a career counselor. Analyze the resume and suggest specific courses, certifications, or projects the student can undertake to fill the gaps in their resume and better match the job description.
"""

recruiter_prompt1 = """
You are an experienced Technical Human Resource Manager. Review the provided resume against the job description and evaluate whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements. Provide a professional evaluation of the candidate's suitability for the role.
"""

recruiter_prompt2 = """
You are an ATS (Applicant Tracking System) scanner. Evaluate the resume against the job description and provide a percentage match. Also, list the missing keywords and provide final thoughts on the resume's compatibility with the job.
"""

# Display different buttons and prompts based on the selected perspective
if option == "Student POV":
    st.subheader("Student Perspective")
    
    # Buttons for Student POV
    if st.button("Get General Feedback"):
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(student_prompt1, pdf_content, input_text)
            st.subheader("General Feedback:")
            st.write(response)
        else:
            st.write("Please upload the resume")
    
    if st.button("Get Skill Gap Analysis"):
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(student_prompt2, pdf_content, input_text)
            st.subheader("Skill Gap Analysis:")
            st.write(response)
        else:
            st.write("Please upload the resume")

elif option == "Recruiter POV":
    st.subheader("Recruiter Perspective")
    
    # Buttons for Recruiter POV
    if st.button("Get Professional Evaluation"):
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(recruiter_prompt1, pdf_content, input_text)
            st.subheader("Professional Evaluation:")
            st.write(response)
        else:
            st.write("Please upload the resume")
    
    if st.button("Check ATS Compatibility"):
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(recruiter_prompt2, pdf_content, input_text)
            st.subheader("ATS Compatibility Check:")
            st.write(response)
        else:
            st.write("Please upload the resume")