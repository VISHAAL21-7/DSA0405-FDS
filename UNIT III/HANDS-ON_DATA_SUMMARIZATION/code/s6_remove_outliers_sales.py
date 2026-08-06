# Dataset: House Sales in King County, USA
# Kaggle: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
import kagglehub
import pandas as pd

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("harlfoxem/housesalesprediction")
df = pd.read_csv(path + "/kc_house_data.csv")

print("Original dataset shape:", df.shape)

# Remove outliers from the 'price' column using the IQR method
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cleaned_df = df[(df["price"] >= lower_bound) & (df["price"] <= upper_bound)]

print("Lower bound:", lower_bound, " Upper bound:", upper_bound)
print("Cleaned dataset shape:", cleaned_df.shape)
print("Rows removed:", df.shape[0] - cleaned_df.shape[0])

print("\nCleaned dataset preview:")
print(cleaned_df[["id", "date", "price", "bedrooms", "bathrooms", "sqft_living"]].head())

# Save the cleaned dataset
cleaned_df.to_csv("kc_house_data_cleaned.csv", index=False)
print("\nCleaned dataset saved as kc_house_data_cleaned.csv")
