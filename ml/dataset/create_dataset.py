import os
import random
import pandas as pd


# ==========================================
# Career Dataset Generator
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "career_dataset.csv"
)

random.seed(42)


# ==========================================
# General Options
# ==========================================

educations = [
    "BCA",
    "B.Tech",
    "B.Sc",
    "MCA",
    "M.Tech"
]

experience_levels = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

problem_solving_levels = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

work_types = [
    "Remote",
    "On-site",
    "Hybrid"
]


# ==========================================
# Career Profiles
# ==========================================

career_profiles = {

    "Web Developer": {
        "programming": [
            "HTML CSS JavaScript",
            "HTML CSS JavaScript PHP",
            "JavaScript HTML CSS",
            "HTML CSS JavaScript Bootstrap"
        ],
        "skills": [
            "HTML CSS JavaScript Bootstrap Responsive Design",
            "JavaScript Bootstrap Responsive Web Design",
            "Frontend Development Responsive Design",
            "HTML CSS JavaScript Web Development"
        ],
        "interests": [
            "Web Development",
            "Website Development",
            "Frontend Development",
            "Full Stack Development"
        ],
        "domain": "Web Development",
        "preference": "Development"
    },


    "Frontend Developer": {
        "programming": [
            "HTML CSS JavaScript",
            "HTML CSS JavaScript React",
            "JavaScript HTML CSS",
            "JavaScript React HTML CSS"
        ],
        "skills": [
            "HTML CSS JavaScript Bootstrap React UI Design",
            "React JavaScript Responsive Design",
            "Frontend Development UI UX Bootstrap",
            "React HTML CSS JavaScript"
        ],
        "interests": [
            "Frontend Development",
            "UI Design",
            "Web Design",
            "User Interface"
        ],
        "domain": "Web Development",
        "preference": "Development"
    },


    "Backend Developer": {
        "programming": [
            "Python Django SQL",
            "Java Spring SQL",
            "Python Django MySQL",
            "Java SQL Backend"
        ],
        "skills": [
            "Django REST API SQL Database Backend Development",
            "Spring Boot REST API SQL",
            "Django MySQL REST API",
            "Backend Development API Database"
        ],
        "interests": [
            "Backend Development",
            "API Development",
            "Server Development",
            "Database Development"
        ],
        "domain": "Software Development",
        "preference": "Development"
    },


    "Python Developer": {
        "programming": [
            "Python",
            "Python Django",
            "Python Flask",
            "Python Django SQL"
        ],
        "skills": [
            "Python Django Flask REST API",
            "Python Django Pandas NumPy",
            "Python Automation API Development",
            "Python Django Backend Development"
        ],
        "interests": [
            "Python Development",
            "Python Programming",
            "Automation",
            "Backend Development"
        ],
        "domain": "Software Development",
        "preference": "Development"
    },


    "Java Developer": {
        "programming": [
            "Java",
            "Java SQL",
            "Java Spring",
            "Java Spring SQL"
        ],
        "skills": [
            "Java Spring Boot Hibernate REST API",
            "Java OOP Spring Boot SQL",
            "Spring Boot REST API Java",
            "Java Backend Development"
        ],
        "interests": [
            "Java Development",
            "Backend Development",
            "Enterprise Applications",
            "Software Development"
        ],
        "domain": "Software Development",
        "preference": "Development"
    },


    "Software Developer": {
        "programming": [
            "Java Python C++",
            "Java Python",
            "C++ Java Python",
            "Java C++"
        ],
        "skills": [
            "DSA OOP Software Development Git",
            "Object Oriented Programming DSA Git",
            "Software Engineering DSA Problem Solving",
            "Algorithms OOP Git Software Development"
        ],
        "interests": [
            "Software Development",
            "Programming",
            "Problem Solving",
            "Application Development"
        ],
        "domain": "Software Development",
        "preference": "Development"
    },


    "Data Analyst": {
        "programming": [
            "Python SQL",
            "Python SQL Excel",
            "SQL Python",
            "Python"
        ],
        "skills": [
            "Pandas NumPy Excel Power BI SQL Data Visualization",
            "Excel SQL Power BI Data Visualization",
            "Pandas NumPy SQL Excel",
            "Power BI Excel SQL Analytics"
        ],
        "interests": [
            "Data Analysis",
            "Business Intelligence",
            "Data Visualization",
            "Analytics"
        ],
        "domain": "Data Science",
        "preference": "Data"
    },


    "Data Scientist": {
        "programming": [
            "Python SQL",
            "Python Pandas NumPy",
            "Python SQL Pandas",
            "Python"
        ],
        "skills": [
            "Pandas NumPy Scikit-learn Statistics Data Analysis",
            "Python Machine Learning Statistics Pandas",
            "Data Science Machine Learning Python",
            "Pandas NumPy Statistics Machine Learning"
        ],
        "interests": [
            "Data Science",
            "Machine Learning",
            "Statistics",
            "Data Analysis"
        ],
        "domain": "Data Science",
        "preference": "Data"
    },


    "ML Engineer": {
        "programming": [
            "Python",
            "Python TensorFlow",
            "Python Scikit-learn",
            "Python Pandas NumPy"
        ],
        "skills": [
            "Machine Learning Scikit-learn TensorFlow Model Deployment",
            "Python Machine Learning Deep Learning TensorFlow",
            "Scikit-learn Pandas NumPy Machine Learning",
            "Artificial Intelligence Machine Learning Python"
        ],
        "interests": [
            "Artificial Intelligence",
            "Machine Learning",
            "Deep Learning",
            "AI Research"
        ],
        "domain": "AI/ML",
        "preference": "Research"
    },


    "Cyber Security Analyst": {
        "programming": [
            "Python Linux",
            "Python Bash",
            "Python Linux Bash",
            "C Python"
        ],
        "skills": [
            "Network Security Ethical Hacking Linux Cyber Security",
            "Cyber Security Penetration Testing Linux",
            "Network Security Cryptography Linux",
            "Ethical Hacking Security Analysis Linux"
        ],
        "interests": [
            "Cyber Security",
            "Ethical Hacking",
            "Network Security",
            "Information Security"
        ],
        "domain": "Cyber Security",
        "preference": "Research"
    },


    "Cloud Engineer": {
        "programming": [
            "Python Linux",
            "Python Bash",
            "Bash Linux",
            "Python"
        ],
        "skills": [
            "AWS Docker Kubernetes Linux Cloud Computing",
            "AWS EC2 Docker Kubernetes",
            "Azure Docker Linux Cloud",
            "Cloud Computing DevOps Docker Linux"
        ],
        "interests": [
            "Cloud Computing",
            "DevOps",
            "Cloud Infrastructure",
            "Deployment"
        ],
        "domain": "Cloud Computing",
        "preference": "Development"
    },


    "Database Administrator": {
        "programming": [
            "SQL",
            "SQL MySQL",
            "SQL PostgreSQL",
            "SQL Oracle"
        ],
        "skills": [
            "MySQL SQL Database Administration Backup Security",
            "PostgreSQL Database Administration SQL",
            "Oracle SQL Database Management",
            "Database Security SQL Backup Recovery"
        ],
        "interests": [
            "Database Management",
            "SQL",
            "Database Administration",
            "Data Management"
        ],
        "domain": "Database",
        "preference": "Data"
    },


    "Android Developer": {
        "programming": [
            "Java Android",
            "Kotlin Android",
            "Java Kotlin",
            "Kotlin"
        ],
        "skills": [
            "Android Studio XML Firebase Mobile Development",
            "Android Development Kotlin Firebase",
            "Java Android Studio XML",
            "Mobile App Development Firebase Android"
        ],
        "interests": [
            "Android Development",
            "Mobile App Development",
            "Application Development",
            "Android Apps"
        ],
        "domain": "Software Development",
        "preference": "Development"
    },


    "PHP Developer": {
        "programming": [
            "PHP MySQL",
            "PHP HTML CSS MySQL",
            "PHP JavaScript MySQL",
            "PHP"
        ],
        "skills": [
            "PHP MySQL Laravel Backend Development",
            "PHP Laravel MySQL",
            "PHP MySQL XAMPP Web Development",
            "Laravel PHP Database Development"
        ],
        "interests": [
            "PHP Development",
            "Laravel",
            "Web Development",
            "Backend Development"
        ],
        "domain": "Web Development",
        "preference": "Development"
    }
}


# ==========================================
# Generate Dataset
# ==========================================

records = []

records_per_career = 50


for career, profile in career_profiles.items():

    for _ in range(records_per_career):

        programming = random.choice(
            profile["programming"]
        )

        skills = random.choice(
            profile["skills"]
        )

        interests = random.choice(
            profile["interests"]
        )

        education = random.choice(
            educations
        )

        experience = random.choice(
            experience_levels
        )

        problem_solving = random.choice(
            problem_solving_levels
        )

        work_type = random.choice(
            work_types
        )

        cgpa = round(
            random.uniform(6.5, 9.7),
            2
        )

        records.append({

            "combined_text":
                f"{programming} {skills} {interests}",

            "education":
                education,

            "experience_level":
                experience,

            "preferred_domain":
                profile["domain"],

            "cgpa":
                cgpa,

            "problem_solving":
                problem_solving,

            "work_preference":
                profile["preference"],

            "work_type":
                work_type,

            "career":
                career
        })


# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(records)


# Shuffle dataset

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# Save CSV

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==========================================
# Information
# ==========================================

print()
print("==========================================")
print("AI Career Dataset Created Successfully!")
print("==========================================")
print(f"Total records: {len(df)}")
print(f"Total careers: {df['career'].nunique()}")
print(f"Records per career: {records_per_career}")
print(f"File: {OUTPUT_FILE}")
print("==========================================")
print()
print("Career Distribution:")
print(df["career"].value_counts())
print()