import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# ==========================================
# Paths
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "dataset",
    "career_dataset.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "ml",
    "model"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "career_model.pkl"
)


# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(DATASET_PATH)

print()
print("==========================================")
print("AI Career Recommendation - Model Training")
print("==========================================")
print(f"Number of records: {len(df)}")
print(f"Number of careers: {df['career'].nunique()}")
print("==========================================")


# ==========================================
# Features
# ==========================================

X = df[
    [
        "combined_text",
        "education",
        "experience_level",
        "preferred_domain",
        "cgpa",
        "problem_solving",
        "work_preference",
        "work_type"
    ]
]

y = df["career"]


# ==========================================
# Train / Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================
# Preprocessing
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[

        (
            "text",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2)
            ),
            "combined_text"
        ),

        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            [
                "education",
                "experience_level",
                "preferred_domain",
                "problem_solving",
                "work_preference",
                "work_type"
            ]
        )
    ],

    remainder="passthrough"
)


# ==========================================
# Random Forest Model
# ==========================================

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)


# ==========================================
# Pipeline
# ==========================================

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", model)
    ]
)


# ==========================================
# Train Model
# ==========================================

print()
print("Training model...")

pipeline.fit(
    X_train,
    y_train
)


# ==========================================
# Evaluate Model
# ==========================================

y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print()
print(f"Test Accuracy: {accuracy * 100:.2f}%")


# ==========================================
# Save Model
# ==========================================

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)

joblib.dump(
    pipeline,
    MODEL_PATH
)

print()
print("Model saved successfully!")
print(f"Model path: {MODEL_PATH}")
print()
print("==========================================")