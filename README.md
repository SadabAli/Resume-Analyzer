# Resume Analyzer

The **Resume Analyzer** project uses an advanced Generative AI model (`gemini-2.0-flash-exp`) to analyze resumes against a specific job description. It provides valuable insights about how well the candidate's resume matches the job requirements.

## Features
- Accepts **Job Description** and **Resume (PDF)** as inputs.
- Generates an analysis report based on the relevance of the resume to the job description.
- User-friendly interface built with **Streamlit**.
- Employs **Generative AI** to craft meaningful and detailed feedback.

## How It Works
1. **Input**:  
   - Enter the **Job Description** in a text box.  
   - Upload the candidate's **Resume (PDF)** file.  
2. **Processing**:  
   - The AI extracts key points from the job description.  
   - The uploaded resume is parsed to identify relevant skills, experiences, and qualifications.  
   - A comparison is made between the job description and the resume content.  
3. **Output**:  
   - Generates a detailed report highlighting strengths, gaps, and recommendations for improvement.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SadabAli/Resume-Analyzer.git
   cd Resume-Analyzer
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment:
   - Add your **Gemini API key** to a `.env` file:
     ```plaintext
     GEMINI_API_KEY=your_gemini_api_key
     ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   
## Example Usage
1. **Job Description Input**:
   ```
   We are looking for a software engineer with expertise in Python, Machine Learning, and Web Development.
   ```
2. **Upload Resume**:  
   A PDF resume with relevant details such as skills, experience, and certifications.
3. **Generated Feedback**:
   - **Strengths**: Strong Python and Machine Learning skills.
   - **Gaps**: Limited web development experience.  
   - **Recommendation**: Add details about web projects or certifications.

## Technologies Used
- **Streamlit**: For the interactive user interface.
- **Gemini-2.0-flash-exp**: Generative AI model for text analysis.
- **Python**: Core programming language.
- **PyPDF2**: For PDF parsing and text extraction.

## Screenshots

![Screenshot 2025-01-16 143701](https://github.com/user-attachments/assets/9a92f334-66ca-484c-9f0d-78cb4e4f7696)

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Special thanks to **OpenAI** for providing the Gemini AI model.
- **Streamlit** for making UI development seamless.
