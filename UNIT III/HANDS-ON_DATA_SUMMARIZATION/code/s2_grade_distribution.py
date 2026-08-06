# Dataset: Students Performance in Exams
# Kaggle: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("spscientist/students-performance-in-exams")
df = pd.read_csv(path + "/StudentsPerformance.csv")

# Convert numeric math score into letter grades
def to_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

df["grade"] = df["math score"].apply(to_grade)

# Frequency distribution of grades
grade_freq = df["grade"].value_counts().sort_index()
print("Frequency Distribution of Grades:")
print(grade_freq)

# Bar chart
plt.figure(figsize=(7, 5))
plt.bar(grade_freq.index, grade_freq.values, color="steelblue")
plt.title("Frequency Distribution of Student Grades (Math Score)")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()
