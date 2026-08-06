# Dataset: 50 Startups
# Kaggle: https://www.kaggle.com/datasets/farhanmd29/50-startups
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("farhanmd29/50-startups")
df = pd.read_csv(path + "/50_Startups.csv")

# Detect and remove outliers in 'Profit' using the IQR method
Q1 = df["Profit"].quantile(0.25)
Q3 = df["Profit"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
cleaned_df = df[(df["Profit"] >= lower_bound) & (df["Profit"] <= upper_bound)]

print(f"Original rows: {len(df)}   Cleaned rows: {len(cleaned_df)}")
print(f"Outliers removed: {len(df) - len(cleaned_df)}")

# Histograms and box plots before and after outlier removal
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].hist(df["Profit"], bins=15, color="steelblue", edgecolor="black")
axes[0, 0].set_title("Histogram - Before Outlier Removal")
axes[0, 0].set_xlabel("Profit ($)")

axes[0, 1].hist(cleaned_df["Profit"], bins=15, color="seagreen", edgecolor="black")
axes[0, 1].set_title("Histogram - After Outlier Removal")
axes[0, 1].set_xlabel("Profit ($)")

axes[1, 0].boxplot(df["Profit"], patch_artist=True, boxprops=dict(facecolor="lightblue"))
axes[1, 0].set_title("Box Plot - Before Outlier Removal")
axes[1, 0].set_ylabel("Profit ($)")

axes[1, 1].boxplot(cleaned_df["Profit"], patch_artist=True, boxprops=dict(facecolor="lightgreen"))
axes[1, 1].set_title("Box Plot - After Outlier Removal")
axes[1, 1].set_ylabel("Profit ($)")

plt.tight_layout()
plt.show()
