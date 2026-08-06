# Dataset: Titanic Dataset
# Kaggle: https://www.kaggle.com/competitions/titanic/data
# (also mirrored at https://www.kaggle.com/datasets/yasserh/titanic-dataset)
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(path + "/Titanic-Dataset.csv")

# 1. Dataset information
print("Dataset shape:", df.shape)
print("\nDataset Info:")
print(df.info())

# 2. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 4. Histograms
df[["Age", "Fare"]].hist(bins=30, figsize=(10, 5), color="steelblue", edgecolor="black")
plt.suptitle("Histograms of Age and Fare")
plt.tight_layout()
plt.show()

# 5. Box plots
plt.figure(figsize=(8, 5))
plt.boxplot([df["Age"].dropna(), df["Fare"].dropna()], labels=["Age", "Fare"],
            patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title("Box Plots of Age and Fare")
plt.tight_layout()
plt.show()

# 6. Detect outliers in Fare using the IQR method
Q1 = df["Fare"].quantile(0.25)
Q3 = df["Fare"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Fare"] < lower_bound) | (df["Fare"] > upper_bound)]
print(f"\nFare outlier bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print("Number of Fare outliers detected:", len(outliers))

# 7. Remove outliers
cleaned_df = df[(df["Fare"] >= lower_bound) & (df["Fare"] <= upper_bound)]
print("Shape before removing outliers:", df.shape)
print("Shape after removing outliers:", cleaned_df.shape)

# 8. Save the cleaned dataset
cleaned_df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned dataset saved as titanic_cleaned.csv")
