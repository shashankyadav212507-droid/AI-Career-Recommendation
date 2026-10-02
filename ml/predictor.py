import os
import joblib
import pandas as pd


# --------------------------------------------------
# MODEL PATH
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "model",
    "career_model.pkl"
)


# --------------------------------------------------
# LOAD ML MODEL
# --------------------------------------------------

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# CAREER INFORMATION
# --------------------------------------------------

CAREER_INFO = {

    "Web Developer": {

        "description":
            "Web Developers create and maintain websites and web applications using frontend and backend technologies.",

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Bootstrap",
            "Responsive Design"
        ],

        "learn": [
            "Advanced JavaScript",
            "React",
            "REST APIs",
            "Git & GitHub"
        ],

        "roadmap": [
            "Learn HTML & CSS",
            "Master JavaScript",
            "Learn Bootstrap & Responsive Design",
            "Learn React",
            "Learn REST APIs",
            "Learn Git & GitHub",
            "Build Real-World Projects",
            "Prepare for Web Development Internships"
        ]

    },


    "Frontend Developer": {

        "description":
            "Frontend Developers build the user interface and client-side functionality of modern websites and web applications.",

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Bootstrap",
            "React"
        ],

        "learn": [
            "Advanced JavaScript",
            "React",
            "UI/UX Basics",
            "REST APIs"
        ],

        "roadmap": [
            "Learn HTML",
            "Master CSS",
            "Learn JavaScript",
            "Learn Bootstrap",
            "Learn React",
            "Learn APIs",
            "Build Responsive Projects",
            "Prepare for Frontend Developer Jobs"
        ]

    },


    "Backend Developer": {

        "description":
            "Backend Developers build server-side applications, APIs, databases and business logic.",

        "skills": [
            "Python",
            "Django",
            "SQL",
            "REST API",
            "Database"
        ],

        "learn": [
            "Django REST Framework",
            "Authentication",
            "API Development",
            "Docker"
        ],

        "roadmap": [
            "Learn Python",
            "Learn SQL & Databases",
            "Learn Django",
            "Learn REST APIs",
            "Learn Authentication",
            "Learn Django REST Framework",
            "Learn Docker",
            "Build Backend Projects"
        ]

    },


    "Python Developer": {

        "description":
            "Python Developers build applications, automation tools, APIs and software using Python and related frameworks.",

        "skills": [
            "Python",
            "Django",
            "Flask",
            "SQL",
            "Git"
        ],

        "learn": [
            "Advanced Python",
            "Django",
            "REST APIs",
            "Testing"
        ],

        "roadmap": [
            "Learn Python Fundamentals",
            "Master OOP in Python",
            "Learn SQL",
            "Learn Django or Flask",
            "Learn REST APIs",
            "Learn Git & GitHub",
            "Build Python Projects",
            "Prepare for Python Developer Internships"
        ]

    },


    "Java Developer": {

        "description":
            "Java Developers create enterprise applications, backend systems and software using Java and related frameworks.",

        "skills": [
            "Java",
            "OOP",
            "Spring Boot",
            "SQL",
            "DSA"
        ],

        "learn": [
            "Spring Boot",
            "REST APIs",
            "Hibernate",
            "Microservices"
        ],

        "roadmap": [
            "Learn Java Fundamentals",
            "Master OOP",
            "Learn Collections & Exception Handling",
            "Practice DSA",
            "Learn SQL",
            "Learn Spring Boot",
            "Build Java Projects",
            "Prepare for Java Developer Jobs"
        ]

    },


    "Software Developer": {

        "description":
            "Software Developers design, develop, test and maintain software applications and systems.",

        "skills": [
            "Programming",
            "DSA",
            "OOP",
            "Git",
            "Problem Solving"
        ],

        "learn": [
            "Advanced DSA",
            "System Design",
            "Git",
            "Software Engineering"
        ],

        "roadmap": [
            "Learn Programming Fundamentals",
            "Master OOP",
            "Learn DSA",
            "Practice Problem Solving",
            "Learn Git & GitHub",
            "Learn Software Engineering",
            "Build Multiple Projects",
            "Prepare for Software Developer Interviews"
        ]

    },


    "Data Analyst": {

        "description":
            "Data Analysts collect, clean, analyze and visualize data to generate useful business insights.",

        "skills": [
            "Python",
            "SQL",
            "Excel",
            "Pandas",
            "Power BI"
        ],

        "learn": [
            "Advanced SQL",
            "Power BI",
            "Statistics",
            "Data Visualization"
        ],

        "roadmap": [
            "Learn Excel",
            "Learn SQL",
            "Learn Python",
            "Learn Pandas & NumPy",
            "Learn Statistics",
            "Learn Power BI",
            "Build Data Analysis Projects",
            "Create a Data Analytics Portfolio"
        ]

    },


    "Data Scientist": {

        "description":
            "Data Scientists use statistics, programming and machine learning to discover patterns and insights from data.",

        "skills": [
            "Python",
            "Pandas",
            "NumPy",
            "Statistics",
            "Machine Learning"
        ],

        "learn": [
            "Machine Learning",
            "Statistics",
            "Scikit-learn",
            "Deep Learning"
        ],

        "roadmap": [
            "Learn Python",
            "Learn NumPy & Pandas",
            "Learn Statistics",
            "Learn Data Visualization",
            "Learn Machine Learning",
            "Learn Scikit-learn",
            "Build ML Projects",
            "Create a Data Science Portfolio"
        ]

    },


    "ML Engineer": {

        "description":
            "Machine Learning Engineers develop, deploy and maintain machine learning models and intelligent applications.",

        "skills": [
            "Python",
            "Machine Learning",
            "Scikit-learn",
            "Pandas",
            "NumPy"
        ],

        "learn": [
            "Deep Learning",
            "TensorFlow",
            "Model Deployment",
            "MLOps"
        ],

        "roadmap": [
            "Learn Python",
            "Learn NumPy & Pandas",
            "Learn Statistics",
            "Learn Machine Learning",
            "Learn Scikit-learn",
            "Learn Deep Learning",
            "Learn Model Deployment",
            "Learn MLOps"
        ]

    },


    "Cyber Security Analyst": {

        "description":
            "Cyber Security Analysts help protect computer systems, networks and applications from security threats.",

        "skills": [
            "Linux",
            "Network Security",
            "Python",
            "Ethical Hacking",
            "Cyber Security"
        ],

        "learn": [
            "Penetration Testing",
            "Cryptography",
            "Network Security",
            "Security Tools"
        ],

        "roadmap": [
            "Learn Computer Networks",
            "Learn Linux",
            "Learn Cyber Security Fundamentals",
            "Learn Python for Security",
            "Learn Ethical Hacking",
            "Learn Cryptography",
            "Practice Security Labs",
            "Prepare for Security Certifications"
        ]

    },


    "Cloud Engineer": {

        "description":
            "Cloud Engineers design, deploy and maintain applications and infrastructure on cloud platforms.",

        "skills": [
            "AWS",
            "Linux",
            "Docker",
            "Kubernetes",
            "Cloud"
        ],

        "learn": [
            "AWS",
            "Docker",
            "Kubernetes",
            "DevOps"
        ],

        "roadmap": [
            "Learn Linux",
            "Learn Networking",
            "Learn Cloud Fundamentals",
            "Learn AWS",
            "Learn Docker",
            "Learn Kubernetes",
            "Learn CI/CD",
            "Build Cloud Projects"
        ]

    },


    "Database Administrator": {

        "description":
            "Database Administrators manage, secure, optimize and maintain databases used by organizations.",

        "skills": [
            "SQL",
            "MySQL",
            "PostgreSQL",
            "Database Administration",
            "Security"
        ],

        "learn": [
            "Advanced SQL",
            "Database Optimization",
            "Backup & Recovery",
            "Database Security"
        ],

        "roadmap": [
            "Learn SQL",
            "Learn MySQL",
            "Learn Database Design",
            "Learn Backup & Recovery",
            "Learn Database Security",
            "Learn Performance Optimization",
            "Practice Database Administration",
            "Build Database Projects"
        ]

    },


    "Android Developer": {

        "description":
            "Android Developers create mobile applications for Android devices using modern development tools and frameworks.",

        "skills": [
            "Java",
            "Kotlin",
            "Android Studio",
            "XML",
            "Firebase"
        ],

        "learn": [
            "Kotlin",
            "Jetpack Compose",
            "Firebase",
            "Android Architecture"
        ],

        "roadmap": [
            "Learn Java or Kotlin",
            "Learn Android Studio",
            "Learn XML & UI Design",
            "Learn Android Components",
            "Learn Firebase",
            "Learn Jetpack Compose",
            "Build Android Applications",
            "Publish Projects & Build Portfolio"
        ]

    },


    "PHP Developer": {

        "description":
            "PHP Developers build dynamic websites and server-side web applications using PHP and database technologies.",

        "skills": [
            "PHP",
            "MySQL",
            "HTML",
            "CSS",
            "Laravel"
        ],

        "learn": [
            "Laravel",
            "REST APIs",
            "MySQL",
            "Authentication"
        ],

        "roadmap": [
            "Learn HTML & CSS",
            "Learn PHP Fundamentals",
            "Learn MySQL",
            "Learn PHP & MySQL Integration",
            "Learn Laravel",
            "Learn REST APIs",
            "Build PHP Projects",
            "Prepare for PHP Developer Jobs"
        ]

    }

}


# --------------------------------------------------
# CAREER INFO HELPER
# --------------------------------------------------

def get_career_info(career):

    return CAREER_INFO.get(
        career,
        {
            "description":
                "Explore this career path by developing relevant technical and professional skills.",

            "skills": [
                "Programming",
                "Problem Solving",
                "Communication"
            ],

            "learn": [
                "Advanced Programming",
                "Projects",
                "Industry Skills"
            ],

            "roadmap": [
                "Learn Fundamentals",
                "Build Technical Skills",
                "Practice Projects",
                "Build Portfolio",
                "Prepare for Internships"
            ]
        }
    )


# --------------------------------------------------
# CAREER PREDICTION
# --------------------------------------------------

def predict_career(data):

    input_df = pd.DataFrame([data])

    probabilities = model.predict_proba(input_df)[0]

    classes = model.classes_

    career_probabilities = list(
        zip(classes, probabilities)
    )

    career_probabilities.sort(
        key=lambda x: x[1],
        reverse=True
    )


    # --------------------------------------------------
    # TOP 3 CAREERS
    # --------------------------------------------------

    top_careers = []

    for career_name, probability in career_probabilities[:3]:

        info = get_career_info(career_name)

        top_careers.append({

            "career": career_name,

            "confidence": round(
                float(probability) * 100,
                2
            ),

            "description":
                info["description"],

            "skills":
                info["skills"],

            "learn":
                info["learn"],

            "roadmap":
                info["roadmap"]

        })


    # --------------------------------------------------
    # PRIMARY CAREER
    # --------------------------------------------------

    primary = top_careers[0]

    return {

        "career":
            primary["career"],

        "confidence":
            primary["confidence"],

        "description":
            primary["description"],

        "skills":
            primary["skills"],

        "learn":
            primary["learn"],

        "roadmap":
            primary["roadmap"],

        "top_careers":
            top_careers

    }