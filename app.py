from flask import Flask, render_template, request
import pickle
import numpy as np

ROLE_SKILLS = {
    "Front-end developer": [
        "html", "css", "javascript", "react", "bootstrap"
    ],
    "Back-end developer": [
        "python", "flask", "django", "sql", "api"
    ],
    "Full stack developer": [
        "html", "css", "javascript", "python", "flask", "sql"
    ],
    "AIML Engineer": [
        "python", "machine learning", "ml", "numpy", "pandas", "scikit-learn"
    ],
    "Data Scientist": [
        "python", "data science", "numpy", "pandas", "machine learning"
    ],
    "UI Designer": [
        "figma", "ui", "design", "wireframe", 	"Good Communication",
	"Learn faster",
	"Computer skills",
	"Management skills",
	"Problem Solving"
    ],
    "UX Designer": [
        "ux", "user research", "prototyping", "usability"
    ],
    "Python developer": [
        "python", "flask", "django", "api"
    ],
    "Java developer": [
      
      "java", "spring", "hibernate", "jdbc"
    ]

}

REQUIRED_SKILLS = [
    "python",
    "machine learning",
    "ml",
    "sklearn",
    "data science",
    "numpy",
    "pandas",
    "scikit-learn",
    "flask",
    "java", "spring", "hibernate", "jdbc","django", "api",
     "ux", "user research", "prototyping", "usability",
     "figma", "ui", "design", "wireframe","html", "css", "javascript", "react", "bootstrap"
	
]

def calculate_skill_match(resume_text,role):
    resume_text = resume_text.lower().replace("\n", " ")
    REQUIRED_SKILLS=ROLE_SKILLS.get(role,[])

    matched_skills = []
    if len(REQUIRED_SKILLS)==0:
            return 0,"Poor",[]
    for skill in REQUIRED_SKILLS:
        if skill in resume_text:
            matched_skills.append(skill)
        if len(REQUIRED_SKILLS)==0:
            return 0,"Poor",[]

    skill_percent = int((len(matched_skills) / len(REQUIRED_SKILLS)) * 100)

    if skill_percent >= 70:
        level = "Good"
    elif skill_percent >= 40:
        level = "Average"
    else:
        level = "Poor"

    return skill_percent, level, matched_skills


app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb")) #loads the logistic regression model

@app.route("/", methods=["GET", "POST"])#GET=page opens,POST= runs when form is submitted
def home():
    #initial values
    status = None
    skill_percent = None
    skill_level = None
    matched_skills = []

    if request.method == "POST":
        resume_file = request.files.get("resume")

        if resume_file:
            resume_text = resume_file.read().decode("utf-8")
            role=request.form["role"]
            skill_percent, skill_level, matched_skills = calculate_skill_match(resume_text,role)

            experience = int(request.form["experience"])
            projects = int(request.form["projects"])
            certificates = int(request.form["certificates"])

            input_data = np.array([[experience, projects, certificates]])
            prediction = model.predict(input_data)[0]

        if prediction == 1 and skill_percent>=40:
            status="Shortlisted"
        else:
            status="Not Shortlisted"

    return render_template(
        "index.html",
        status=status,
        skill_percent=skill_percent,
        skill_level=skill_level,
        matched_skills=matched_skills
    )

if __name__ == "__main__":
    app.run(debug=True)