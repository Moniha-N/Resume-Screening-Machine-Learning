Project :Resume Shortlisting  System

A Machine Learning based Resume Shortlisting System developed using Python, Flask, and Logistic Regression. This project analyzes text-based resume details and predicts whether a candidate is shortlisted or not.

Features:

- Resume screening using Machine Learning
- Predicts shortlisted or not shortlisted result
- Displays match percentage and skill level
- User-friendly web interface
- Fast prediction system

Technologies Used:

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Logistic Regression

Project Structure

Resume-Shortlisting-System/
│
├── static/
├── templates/
├── app.py
├── model.py
├── model.pkl
├── resume_data.csv
├── requirements.txt
├── README.md
└── .gitignore

How It Works

1. User enters resume details.
2. Flask backend sends data to ML model.
3. Logistic Regression model analyzes the input.
4. System displays:
   - Match Percentage
   - Skill Level
   - Matched Skills
   - Shortlisted / Not Shortlisted Result

Installation

'''bash
git clone https://github.com/Moniha-N/Resume-Screening-Machine-Learning.git
cd Resume-Screening-Machine-Learning
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
'''
Open:
http://127.0.0.1:5000

Future Improvements

- PDF Resume Upload
- Better UI/UX
- NLP Integration
- Cloud Deployment

  Author
- Moniha N