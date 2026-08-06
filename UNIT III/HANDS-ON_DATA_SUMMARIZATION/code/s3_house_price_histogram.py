# Dataset: House Sales in King County, USA
# Kaggle: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("harlfoxem/housesalesprediction")
df = pd.read_csv(path + "/kc_house_data.csv")

# Plot histogram of house prices
plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=60, color="teal", edgecolor="black")
plt.title("Distribution of House Prices")
plt.xlabel("Price ($)")
plt.ylabel("Number of Houses")
plt.tight_layout()
plt.show()

# Check skewness
price_skew = skew(df["price"])
print("Skewness of house price distribution:", round(price_skew, 3))

if price_skew > 0.5:
    print("The data is right-skewed (positively skewed).")
elif price_skew < -0.5:
    print("The data is left-skewed (negatively skewed).")
else:
    print("The data is approximately normally distributed.")
